"""Run repeatable benchmark prompts against the local Ollama API."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from lib.api import DEFAULT_API_URL, call_ollama, detect_run_type
from lib.environment import collect_environment_metadata
from lib.prompts import list_prompt_paths, read_prompt, resolve_prompt_path
from lib.reports import (
    write_json_result,
    write_markdown_result,
    write_master_summary_json,
    write_master_summary_markdown,
    write_summary_json,
    write_summary_markdown,
)
from lib.results import (
    build_master_summary_record,
    build_result_record,
    build_summary_record,
)
from lib.utils import RESULTS_DIR, safe_path_component

DEFAULT_MODEL = "qwen3:8b"


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Run benchmark prompts against a local Ollama model."
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        help="Prompt filename or name, for example finnish or finnish.md.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        dest="run_all",
        help="Run every Markdown prompt in the prompts directory.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Ollama model name. Default: {DEFAULT_MODEL}",
    )
    parser.add_argument(
        "--think",
        choices=("on", "off"),
        default="off",
        help="Enable or disable model reasoning. Default: off",
    )
    parser.add_argument(
        "--repeat",
        type=int,
        default=1,
        help="Number of runs for each prompt. Default: 1",
    )
    parser.add_argument(
        "--api-url",
        default=DEFAULT_API_URL,
        help=f"Ollama generate endpoint. Default: {DEFAULT_API_URL}",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=600,
        help="HTTP request timeout in seconds. Default: 600",
    )
    return parser.parse_args()


def validate_arguments(args: argparse.Namespace) -> None:
    """Validate command-line argument combinations and values."""
    if args.repeat < 1:
        raise ValueError("--repeat must be at least 1.")

    if args.run_all and args.prompt:
        raise ValueError("Use either a prompt name or --all, not both.")

    if not args.run_all and not args.prompt:
        raise ValueError("Provide a prompt name or use --all.")


def select_prompt_paths(args: argparse.Namespace) -> list[Path]:
    """Select one prompt or every available prompt."""
    if args.run_all:
        prompt_paths = list_prompt_paths()

        if not prompt_paths:
            raise FileNotFoundError("No Markdown prompt files were found.")

        return prompt_paths

    return [resolve_prompt_path(args.prompt)]


def run_single_benchmark(
    *,
    prompt_name: str,
    prompt_text: str,
    model: str,
    think_enabled: bool,
    api_url: str,
    timeout: int,
    run_number: int,
    total_runs: int,
    batch_timestamp: str,
    environment: dict[str, Any],
) -> dict[str, Any]:
    """Run and store one benchmark execution."""
    run_type = detect_run_type(
        generate_api_url=api_url,
        model=model,
        timeout=timeout,
    )

    print()
    print(f"Run {run_number}/{total_runs}")
    print(f"Model: {model}")
    print(f"Prompt: {prompt_name}")
    print(f"Thinking: {'on' if think_enabled else 'off'}")
    print(f"Run type: {run_type}")
    print("Running benchmark...")

    result = call_ollama(
        api_url=api_url,
        model=model,
        prompt=prompt_text,
        think_enabled=think_enabled,
        timeout=timeout,
    )

    record = build_result_record(
        result=result,
        prompt_name=prompt_name,
        prompt_text=prompt_text,
        model=model,
        think_enabled=think_enabled,
        run_type=run_type,
        run_number=run_number,
        total_runs=total_runs,
        batch_timestamp=batch_timestamp,
        environment=environment,
    )

    model_dir = RESULTS_DIR / safe_path_component(model)
    model_dir.mkdir(parents=True, exist_ok=True)

    think_label = "on" if think_enabled else "off"
    output_base = model_dir / (
        f"{batch_timestamp}_{Path(prompt_name).stem}_"
        f"think-{think_label}_{run_type}_run-{run_number}"
    )

    json_path = write_json_result(record, output_base)
    markdown_path = write_markdown_result(record, output_base)

    metrics = record["metrics"]

    print("Benchmark completed.")
    print(f"Run type: {run_type}")
    print(f"Total duration: {metrics['total_duration_seconds']} s")
    print(f"Generated tokens: {metrics['eval_count']}")
    print(f"Generation speed: {metrics['tokens_per_second']} tokens/s")
    print(f"JSON result: {json_path}")
    print(f"Markdown result: {markdown_path}")

    return record


def run_prompt_batch(
    *,
    prompt_path: Path,
    model: str,
    think_enabled: bool,
    repeat: int,
    api_url: str,
    timeout: int,
    batch_timestamp: str,
    environment: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Run all requested repetitions for one prompt."""
    prompt_text = read_prompt(prompt_path)
    records: list[dict[str, Any]] = []

    print()
    print("=" * 72)
    print(f"Prompt batch: {prompt_path.name}")
    print("=" * 72)

    for run_number in range(1, repeat + 1):
        record = run_single_benchmark(
            prompt_name=prompt_path.name,
            prompt_text=prompt_text,
            model=model,
            think_enabled=think_enabled,
            api_url=api_url,
            timeout=timeout,
            run_number=run_number,
            total_runs=repeat,
            batch_timestamp=batch_timestamp,
            environment=environment,
        )
        records.append(record)

    summary = build_summary_record(records)

    if repeat > 1:
        model_dir = RESULTS_DIR / safe_path_component(model)
        think_label = "on" if think_enabled else "off"
        summary_base = model_dir / (
            f"{batch_timestamp}_{prompt_path.stem}_"
            f"think-{think_label}_repeat-{repeat}_summary"
        )

        write_summary_json(summary, summary_base)
        write_summary_markdown(summary, summary_base)

    return records, summary


def main() -> int:
    """Run selected benchmarks and save result reports."""
    args = parse_arguments()

    try:
        validate_arguments(args)
        prompt_paths = select_prompt_paths(args)
        batch_timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        think_enabled = args.think == "on"
        environment = collect_environment_metadata(
            generate_api_url=args.api_url,
            model=args.model,
            timeout=args.timeout,
        )

        print("Environment metadata collected.")
        print(f"Python: {environment['python_version']}")
        print(f"Ollama: {environment['ollama_version']}")
        print(
            "Model: "
            f"{environment['model']['parameter_size']} "
            f"{environment['model']['quantization_level']}"
        )

        all_records: list[dict[str, Any]] = []
        prompt_summaries: list[dict[str, Any]] = []

        for prompt_path in prompt_paths:
            records, summary = run_prompt_batch(
                prompt_path=prompt_path,
                model=args.model,
                think_enabled=think_enabled,
                repeat=args.repeat,
                api_url=args.api_url,
                timeout=args.timeout,
                batch_timestamp=batch_timestamp,
                environment=environment,
            )
            all_records.extend(records)
            prompt_summaries.append(summary)

        if args.run_all:
            master_summary = build_master_summary_record(
                records=all_records,
                prompt_summaries=prompt_summaries,
            )

            model_dir = RESULTS_DIR / safe_path_component(args.model)
            think_label = "on" if think_enabled else "off"
            master_base = model_dir / (
                f"{batch_timestamp}_all-prompts_"
                f"think-{think_label}_repeat-{args.repeat}_master-summary"
            )

            write_master_summary_json(master_summary, master_base)
            write_master_summary_markdown(master_summary, master_base)

        return 0

    except (
        FileNotFoundError,
        ValueError,
        RuntimeError,
        json.JSONDecodeError,
    ) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
