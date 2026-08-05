"""Run repeatable benchmark prompts against the local Ollama API."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

from lib.api import DEFAULT_API_URL, call_ollama, detect_run_type
from lib.prompts import read_prompt, resolve_prompt_path
from lib.reports import (
    write_json_result,
    write_markdown_result,
    write_summary_json,
    write_summary_markdown,
)
from lib.results import build_result_record, build_summary_record
from lib.utils import RESULTS_DIR, safe_path_component

DEFAULT_MODEL = "qwen3:8b"


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Run benchmark prompts against a local Ollama model."
    )
    parser.add_argument(
        "prompt",
        help="Prompt filename or name, for example finnish or finnish.md.",
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
        help="Number of benchmark runs. Default: 1",
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
    """Validate command-line argument values."""
    if args.repeat < 1:
        raise ValueError("--repeat must be at least 1.")


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
) -> dict:
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


def main() -> int:
    """Run one or more benchmarks and save results and summaries."""
    args = parse_arguments()

    try:
        validate_arguments(args)
        prompt_path = resolve_prompt_path(args.prompt)
        prompt_text = read_prompt(prompt_path)
        batch_timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

        records = []

        for run_number in range(1, args.repeat + 1):
            record = run_single_benchmark(
                prompt_name=prompt_path.name,
                prompt_text=prompt_text,
                model=args.model,
                think_enabled=args.think == "on",
                api_url=args.api_url,
                timeout=args.timeout,
                run_number=run_number,
                total_runs=args.repeat,
                batch_timestamp=batch_timestamp,
            )
            records.append(record)

        if args.repeat > 1:
            summary = build_summary_record(records)

            model_dir = RESULTS_DIR / safe_path_component(args.model)
            summary_base = model_dir / (
                f"{batch_timestamp}_{prompt_path.stem}_"
                f"think-{args.think}_repeat-{args.repeat}_summary"
            )

            summary_json_path = write_summary_json(summary, summary_base)
            summary_markdown_path = write_summary_markdown(summary, summary_base)

            stats = summary["statistics"]

            print()
            print("Benchmark summary")
            print(f"Runs: {summary['run_count']}")
            print(f"Cold runs: {summary['cold_run_count']}")
            print(f"Warm runs: {summary['warm_run_count']}")
            print(
                "Average total duration: "
                f"{stats['total_duration_seconds']['mean']} s"
            )
            print(
                "Median total duration: "
                f"{stats['total_duration_seconds']['median']} s"
            )
            print(
                "Average generation speed: "
                f"{stats['tokens_per_second']['mean']} tokens/s"
            )
            print(f"Summary JSON: {summary_json_path}")
            print(f"Summary Markdown: {summary_markdown_path}")

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
