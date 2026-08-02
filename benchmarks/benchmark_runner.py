"""Run repeatable benchmark prompts against the local Ollama API."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any


DEFAULT_API_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "qwen3:8b"

SCRIPT_DIR = Path(__file__).resolve().parent
PROMPTS_DIR = SCRIPT_DIR / "prompts"
RESULTS_DIR = SCRIPT_DIR / "results"


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


def resolve_prompt_path(prompt_name: str) -> Path:
    """Resolve a prompt name to a Markdown file in the prompts directory."""

    candidate = Path(prompt_name)

    if candidate.suffix.lower() != ".md":
        candidate = candidate.with_suffix(".md")

    prompt_path = PROMPTS_DIR / candidate.name

    if not prompt_path.is_file():
        available = ", ".join(
            sorted(path.name for path in PROMPTS_DIR.glob("*.md"))
        )

        raise FileNotFoundError(
            f"Prompt not found: {prompt_path}\n"
            f"Available prompts: {available or 'none'}"
        )

    return prompt_path


def read_prompt(prompt_path: Path) -> str:
    """Read and validate a benchmark prompt."""

    prompt = prompt_path.read_text(encoding="utf-8").strip()

    if not prompt:
        raise ValueError(f"Prompt file is empty: {prompt_path}")

    return prompt


def call_ollama(
    *,
    api_url: str,
    model: str,
    prompt: str,
    think_enabled: bool,
    timeout: int,
) -> dict[str, Any]:
    """Send a non-streaming generation request to the Ollama API."""

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "think": think_enabled,
        "options": {
            "temperature": 0,
            "seed": 42,
            "num_ctx": 4096,
        },
    }

    request = urllib.request.Request(
        api_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            response_data = response.read().decode("utf-8")

    except urllib.error.HTTPError as error:
        details = error.read().decode("utf-8", errors="replace")

        raise RuntimeError(
            f"Ollama returned HTTP {error.code}: {details}"
        ) from error

    except urllib.error.URLError as error:
        raise RuntimeError(
            "Could not connect to Ollama. Confirm that Ollama is running at "
            f"{api_url}."
        ) from error

    result = json.loads(response_data)

    if not result.get("done", False):
        raise RuntimeError("Ollama did not return a completed response.")

    return result


def nanoseconds_to_seconds(value: int | float | None) -> float:
    """Convert nanoseconds to seconds."""

    return float(value or 0) / 1_000_000_000


def calculate_tokens_per_second(
    result: dict[str, Any],
) -> float | None:
    """Calculate token generation speed from Ollama response metrics."""

    token_count = result.get("eval_count")
    duration_ns = result.get("eval_duration")

    if not token_count or not duration_ns:
        return None

    duration_seconds = nanoseconds_to_seconds(duration_ns)

    if duration_seconds == 0:
        return None

    return float(token_count) / duration_seconds


def safe_path_component(value: str) -> str:
    """Convert a model name into a filesystem-safe directory name."""

    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", value)
    return cleaned.strip("-").lower() or "unknown"


def build_result_record(
    *,
    result: dict[str, Any],
    prompt_name: str,
    prompt_text: str,
    model: str,
    think_enabled: bool,
) -> dict[str, Any]:
    """Build the normalized benchmark result record."""

    tokens_per_second = calculate_tokens_per_second(result)

    return {
        "benchmark_timestamp": datetime.now().astimezone().isoformat(),
        "prompt_name": prompt_name,
        "model": model,
        "think_enabled": think_enabled,
        "context_size": 4096,
        "temperature": 0,
        "seed": 42,
        "prompt": prompt_text,
        "response": result.get("response", ""),
        "thinking": result.get("thinking", ""),
        "done_reason": result.get("done_reason"),
        "metrics": {
            "total_duration_seconds": round(
                nanoseconds_to_seconds(result.get("total_duration")),
                3,
            ),
            "load_duration_seconds": round(
                nanoseconds_to_seconds(result.get("load_duration")),
                3,
            ),
            "prompt_eval_count": result.get("prompt_eval_count"),
            "prompt_eval_duration_seconds": round(
                nanoseconds_to_seconds(
                    result.get("prompt_eval_duration")
                ),
                3,
            ),
            "eval_count": result.get("eval_count"),
            "eval_duration_seconds": round(
                nanoseconds_to_seconds(result.get("eval_duration")),
                3,
            ),
            "tokens_per_second": (
                round(tokens_per_second, 2)
                if tokens_per_second is not None
                else None
            ),
        },
    }


def write_json_result(
    record: dict[str, Any],
    output_base: Path,
) -> Path:
    """Write the complete benchmark result as JSON."""

    output_path = output_base.with_suffix(".json")

    output_path.write_text(
        json.dumps(record, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    return output_path


def write_markdown_result(
    record: dict[str, Any],
    output_base: Path,
) -> Path:
    """Write a human-readable benchmark report as Markdown."""

    metrics = record["metrics"]
    thinking_label = "on" if record["think_enabled"] else "off"

    thinking_section = ""

    if record["think_enabled"]:
        thinking_text = record["thinking"].strip()

        thinking_section = (
            "\n## Thinking output\n\n"
            "```text\n"
            f"{thinking_text or '[No separate thinking output returned]'}\n"
            "```\n"
        )

    markdown = (
        "# Benchmark Result\n\n"
        "## Configuration\n\n"
        "| Item | Value |\n"
        "|---|---|\n"
        f'| Timestamp | `{record["benchmark_timestamp"]}` |\n'
        f'| Model | `{record["model"]}` |\n'
        f'| Prompt | `{record["prompt_name"]}` |\n'
        f"| Thinking | `{thinking_label}` |\n"
        f'| Context size | `{record["context_size"]}` |\n'
        f'| Temperature | `{record["temperature"]}` |\n'
        f'| Seed | `{record["seed"]}` |\n\n'
        "## Metrics\n\n"
        "| Metric | Value |\n"
        "|---|---:|\n"
        f'| Total duration | {metrics["total_duration_seconds"]} s |\n'
        f'| Model load duration | {metrics["load_duration_seconds"]} s |\n'
        f'| Prompt tokens | {metrics["prompt_eval_count"]} |\n'
        f'| Prompt evaluation duration | {metrics["prompt_eval_duration_seconds"]} s |\n'
        f'| Generated tokens | {metrics["eval_count"]} |\n'
        f'| Generation duration | {metrics["eval_duration_seconds"]} s |\n'
        f'| Generation speed | {metrics["tokens_per_second"]} tokens/s |\n\n'
        "## Prompt\n\n"
        "```text\n"
        f'{record["prompt"]}\n'
        "```\n\n"
        "## Response\n\n"
        f'{record["response"].strip()}\n'
        f"{thinking_section}\n"
    )

    output_path = output_base.with_suffix(".md")
    output_path.write_text(markdown, encoding="utf-8")

    return output_path


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
        print(
            "Generation speed: "
            f"{metrics['tokens_per_second']} tokens/s"
        )
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