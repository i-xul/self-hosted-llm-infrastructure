"""JSON and Markdown benchmark report generation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def write_json_result(record: dict[str, Any], output_base: Path) -> Path:
    """Write the complete benchmark result as JSON."""
    output_path = output_base.with_suffix(".json")
    output_path.write_text(
        json.dumps(record, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return output_path


def write_markdown_result(record: dict[str, Any], output_base: Path) -> Path:
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
        f'| Batch timestamp | `{record["batch_timestamp"]}` |\n'
        f'| Run | `{record["run_number"]}/{record["total_runs"]}` |\n'
        f'| Model | `{record["model"]}` |\n'
        f'| Prompt | `{record["prompt_name"]}` |\n'
        f'| Run type | `{record["run_type"]}` |\n'
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


def write_summary_json(summary: dict[str, Any], output_base: Path) -> Path:
    """Write aggregate benchmark statistics as JSON."""
    output_path = output_base.with_suffix(".json")
    output_path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return output_path


def _format_stat(value: float | None) -> str:
    """Format an optional numeric statistic for Markdown."""
    return "N/A" if value is None else str(value)


def write_summary_markdown(summary: dict[str, Any], output_base: Path) -> Path:
    """Write aggregate benchmark statistics as Markdown."""
    think_label = "on" if summary["think_enabled"] else "off"
    stats = summary["statistics"]

    run_rows = "\n".join(
        "| {run_number} | {run_type} | {total} s | {load} s | {tokens} | {speed} tok/s |".format(
            run_number=run["run_number"],
            run_type=run["run_type"],
            total=run["total_duration_seconds"],
            load=run["load_duration_seconds"],
            tokens=run["generated_tokens"],
            speed=run["tokens_per_second"],
        )
        for run in summary["runs"]
    )

    labels = {
        "total_duration_seconds": "Total duration (s)",
        "load_duration_seconds": "Model load duration (s)",
        "generated_tokens": "Generated tokens",
        "generation_duration_seconds": "Generation duration (s)",
        "tokens_per_second": "Generation speed (tokens/s)",
    }

    statistic_rows = []
    for key, label in labels.items():
        values = stats[key]
        statistic_rows.append(
            "| {label} | {mean} | {median} | {minimum} | {maximum} |".format(
                label=label,
                mean=_format_stat(values["mean"]),
                median=_format_stat(values["median"]),
                minimum=_format_stat(values["minimum"]),
                maximum=_format_stat(values["maximum"]),
            )
        )

    markdown = (
        "# Repeated Benchmark Summary\n\n"
        "## Configuration\n\n"
        "| Item | Value |\n"
        "|---|---|\n"
        f'| Summary timestamp | `{summary["summary_timestamp"]}` |\n'
        f'| Batch timestamp | `{summary["batch_timestamp"]}` |\n'
        f'| Model | `{summary["model"]}` |\n'
        f'| Prompt | `{summary["prompt_name"]}` |\n'
        f"| Thinking | `{think_label}` |\n"
        f'| Context size | `{summary["context_size"]}` |\n'
        f'| Temperature | `{summary["temperature"]}` |\n'
        f'| Seed | `{summary["seed"]}` |\n'
        f'| Runs | `{summary["run_count"]}` |\n'
        f'| Cold runs | `{summary["cold_run_count"]}` |\n'
        f'| Warm runs | `{summary["warm_run_count"]}` |\n\n'
        "## Aggregate Statistics\n\n"
        "| Metric | Mean | Median | Minimum | Maximum |\n"
        "|---|---:|---:|---:|---:|\n"
        + "\n".join(statistic_rows)
        + "\n\n"
        "## Individual Runs\n\n"
        "| Run | Type | Total duration | Load duration | Generated tokens | Generation speed |\n"
        "|---:|---|---:|---:|---:|---:|\n"
        f"{run_rows}\n"
    )

    output_path = output_base.with_suffix(".md")
    output_path.write_text(markdown, encoding="utf-8")
    return output_path
