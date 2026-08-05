"""Run repeatable benchmark prompts against the local Ollama API."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime

from lib.api import DEFAULT_API_URL, call_ollama
from lib.prompts import read_prompt, resolve_prompt_path
from lib.reports import write_json_result, write_markdown_result
from lib.results import build_result_record
from lib.utils import RESULTS_DIR, safe_path_component

DEFAULT_MODEL = "qwen3:8b"


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Run a benchmark prompt against a local Ollama model."
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


def main() -> int:
    """Run one benchmark and save its results."""
    args = parse_arguments()

    try:
        prompt_path = resolve_prompt_path(args.prompt)
        prompt_text = read_prompt(prompt_path)

        print(f"Model: {args.model}")
        print(f"Prompt: {prompt_path.name}")
        print(f"Thinking: {args.think}")
        print("Running benchmark...")

        result = call_ollama(
            api_url=args.api_url,
            model=args.model,
            prompt=prompt_text,
            think_enabled=args.think == "on",
            timeout=args.timeout,
        )

        record = build_result_record(
            result=result,
            prompt_name=prompt_path.name,
            prompt_text=prompt_text,
            model=args.model,
            think_enabled=args.think == "on",
        )

        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        model_dir = RESULTS_DIR / safe_path_component(args.model)
        model_dir.mkdir(parents=True, exist_ok=True)
        output_base = model_dir / (
            f"{timestamp}_{prompt_path.stem}_think-{args.think}"
        )

        json_path = write_json_result(record, output_base)
        markdown_path = write_markdown_result(record, output_base)

        metrics = record["metrics"]

        print()
        print("Benchmark completed.")
        print(f"Total duration: {metrics['total_duration_seconds']} s")
        print(f"Generated tokens: {metrics['eval_count']}")
        print(f"Generation speed: {metrics['tokens_per_second']} tokens/s")
        print(f"JSON result: {json_path}")
        print(f"Markdown result: {markdown_path}")
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
