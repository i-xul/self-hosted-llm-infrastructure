#!/usr/bin/env python3
#
# ----------------------------------------------------------------------
# Self-Hosted LLM Infrastructure
# ----------------------------------------------------------------------
#
# Author: H A (i-xul)
# Repository: https://github.com/i-xul/self-hosted-llm-infrastructure
#
# File: benchmarks/lib/reports.py
# Created: 2026-08-05
# Version: v1.0.0
#
# Purpose:
# Writes individual, repeated, and all-prompts benchmark reports in
# JSON and human-readable Markdown formats.
#
# Workflow:
# 1. Write consistently formatted JSON files.
# 2. Render environment metadata.
# 3. Write individual benchmark reports.
# 4. Write repeated-run summaries.
# 5. Write all-prompts master summaries.
#
# ----------------------------------------------------------------------

"""JSON and Markdown benchmark report generation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


# =============================================================================
# Shared JSON and formatting helpers
# =============================================================================

def _write_json(data: dict[str, Any], output_base: Path) -> Path:
    """
    Write JSON data with stable UTF-8 and indentation settings.
    """

    output_path = output_base.with_suffix(".json")

    output_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    return output_path


def _environment_markdown(environment: dict[str, Any]) -> str:
    """
    Render environment and model metadata as a Markdown table.
    """

    model = environment.get("model", {})
    families = ", ".join(model.get("families") or []) or "N/A"

    return (
        "## Environment\n\n"
        "| Item | Value |\n"
        "|---|---|\n"
        f'| Operating system | `{environment.get("operating_system")}` |\n'
        f'| Machine architecture | `{environment.get("machine_architecture")}` |\n'
        f'| Python version | `{environment.get("python_version")}` |\n'
        f'| Python implementation | `{environment.get("python_implementation")}` |\n'
        f'| Ollama version | `{environment.get("ollama_version")}` |\n'
        f'| Model format | `{model.get("format")}` |\n'
        f'| Model family | `{model.get("family")}` |\n'
        f'| Model families | `{families}` |\n'
        f'| Parameter size | `{model.get("parameter_size")}` |\n'
        f'| Quantization | `{model.get("quantization_level")}` |\n'
        f'| Model context length | `{model.get("context_length")}` |\n\n'
    )


# =============================================================================
# Individual benchmark reports
# =============================================================================

def write_json_result(
    record: dict[str, Any],
    output_base: Path,
) -> Path:
    """
    Write one complete benchmark result as JSON.
    """

    return _write_json(record, output_base)


def _resource_usage_markdown(resources: dict[str, Any] | None) -> str:
    """
    Format runtime RAM and inference-GPU VRAM usage as Markdown.
    """

    if not resources:
        return (
            "## Resource Usage\n\n"
            "Resource monitoring was unavailable for this benchmark run.\n\n"
        )

    system_memory = resources.get("system_memory")
    inference_gpu = resources.get("inference_gpu")
    sampling_error = resources.get("sampling_error")

    rows: list[str] = []

    if system_memory:
        rows.append(
            "| System RAM | "
            f'{system_memory["before_gib"]} GiB | '
            f'{system_memory["peak_gib"]} GiB | '
            f'{system_memory["after_gib"]} GiB | '
            f'{system_memory["peak_delta_gib"]} GiB |'
        )

    if inference_gpu:
        rows.append(
            "| Inference GPU VRAM | "
            f'{inference_gpu["before_gib"]} GiB | '
            f'{inference_gpu["peak_gib"]} GiB | '
            f'{inference_gpu["after_gib"]} GiB | '
            f'{inference_gpu["peak_delta_gib"]} GiB |'
        )

    if not rows:
        rows.append("| No resource data available | - | - | - | - |")

    markdown = (
        "## Resource Usage\n\n"
        "| Resource | Before | Peak | After | Peak delta |\n"
        "|---|---:|---:|---:|---:|\n"
        + "\n".join(rows)
        + "\n\n"
    )

    if sampling_error:
        markdown += (
            f"Resource monitoring warning: `{sampling_error}`\n\n"
        )

    return markdown


def _resource_statistics_markdown(
    title: str,
    statistics: dict[str, dict[str, float | None]],
) -> str:
    """
    Format aggregate resource statistics as a Markdown table.
    """

    return (
        f"## {title}\n\n"
        "| Resource metric | Mean | Median | Minimum | Maximum |\n"
        "|---|---:|---:|---:|---:|\n"
        "| System RAM peak (GiB) | "
        f'{statistics["system_memory_peak_gib"]["mean"]} | '
        f'{statistics["system_memory_peak_gib"]["median"]} | '
        f'{statistics["system_memory_peak_gib"]["minimum"]} | '
        f'{statistics["system_memory_peak_gib"]["maximum"]} |\n'
        "| System RAM peak delta (GiB) | "
        f'{statistics["system_memory_peak_delta_gib"]["mean"]} | '
        f'{statistics["system_memory_peak_delta_gib"]["median"]} | '
        f'{statistics["system_memory_peak_delta_gib"]["minimum"]} | '
        f'{statistics["system_memory_peak_delta_gib"]["maximum"]} |\n'
        "| Inference GPU VRAM peak (GiB) | "
        f'{statistics["inference_gpu_peak_gib"]["mean"]} | '
        f'{statistics["inference_gpu_peak_gib"]["median"]} | '
        f'{statistics["inference_gpu_peak_gib"]["minimum"]} | '
        f'{statistics["inference_gpu_peak_gib"]["maximum"]} |\n'
        "| Inference GPU VRAM peak delta (GiB) | "
        f'{statistics["inference_gpu_peak_delta_gib"]["mean"]} | '
        f'{statistics["inference_gpu_peak_delta_gib"]["median"]} | '
        f'{statistics["inference_gpu_peak_delta_gib"]["minimum"]} | '
        f'{statistics["inference_gpu_peak_delta_gib"]["maximum"]} |\n\n'
    )


def write_markdown_result(
    record: dict[str, Any],
    output_base: Path,
) -> Path:
    """
    Write one complete benchmark result as Markdown.
    """

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
        + _environment_markdown(record["environment"])
        + "## Metrics\n\n"
        "| Metric | Value |\n"
        "|---|---:|\n"
        f'| Total duration | {metrics["total_duration_seconds"]} s |\n'
        f'| Model load duration | {metrics["load_duration_seconds"]} s |\n'
        f'| Prompt tokens | {metrics["prompt_eval_count"]} |\n'
        f'| Prompt evaluation duration | '
        f'{metrics["prompt_eval_duration_seconds"]} s |\n'
        f'| Generated tokens | {metrics["eval_count"]} |\n'
        f'| Generation duration | {metrics["eval_duration_seconds"]} s |\n'
        f'| Generation speed | {metrics["tokens_per_second"]} tokens/s |\n\n'
        + _resource_usage_markdown(record.get("resources"))
        + "## Prompt\n\n"
        "```text\n"
        f'{record["prompt"]}\n'
        "```\n\n"
        "## Response\n\n"
        f'{record["response"].strip()}\n'
        f"{thinking_section}"
    )

    output_path = output_base.with_suffix(".md")
    output_path.write_text(markdown, encoding="utf-8")

    return output_path


# =============================================================================
# Repeated-run summary reports
# =============================================================================

def write_summary_json(
    summary: dict[str, Any],
    output_base: Path,
) -> Path:
    """
    Write one prompt's aggregate statistics as JSON.
    """

    return _write_json(summary, output_base)


def write_summary_markdown(
    summary: dict[str, Any],
    output_base: Path,
) -> Path:
    """
    Write one prompt's aggregate statistics as Markdown.
    """

    stats = summary["statistics"]
    resource_stats = summary.get("resource_statistics", {})
    think_label = "on" if summary["think_enabled"] else "off"

    run_rows = "\n".join(
        "| {run_number} | {run_type} | {total} s | {load} s | "
        "{tokens} | {speed} tok/s |".format(
            run_number=run["run_number"],
            run_type=run["run_type"],
            total=run["total_duration_seconds"],
            load=run["load_duration_seconds"],
            tokens=run["generated_tokens"],
            speed=run["tokens_per_second"],
        )
        for run in summary["runs"]
    )

    markdown = (
        "# Repeated Benchmark Summary\n\n"
        "## Configuration\n\n"
        "| Item | Value |\n"
        "|---|---|\n"
        f'| Model | `{summary["model"]}` |\n'
        f'| Prompt | `{summary["prompt_name"]}` |\n'
        f"| Thinking | `{think_label}` |\n"
        f'| Runs | `{summary["run_count"]}` |\n'
        f'| Cold runs | `{summary["cold_run_count"]}` |\n'
        f'| Warm runs | `{summary["warm_run_count"]}` |\n\n'
        + _environment_markdown(summary["environment"])
        + "## Aggregate Statistics\n\n"
        "| Metric | Mean | Median | Minimum | Maximum |\n"
        "|---|---:|---:|---:|---:|\n"
        f'| Total duration (s) | {stats["total_duration_seconds"]["mean"]} | '
        f'{stats["total_duration_seconds"]["median"]} | '
        f'{stats["total_duration_seconds"]["minimum"]} | '
        f'{stats["total_duration_seconds"]["maximum"]} |\n'
        f'| Generated tokens | {stats["generated_tokens"]["mean"]} | '
        f'{stats["generated_tokens"]["median"]} | '
        f'{stats["generated_tokens"]["minimum"]} | '
        f'{stats["generated_tokens"]["maximum"]} |\n'
        f'| Generation speed (tokens/s) | {stats["tokens_per_second"]["mean"]} | '
        f'{stats["tokens_per_second"]["median"]} | '
        f'{stats["tokens_per_second"]["minimum"]} | '
        f'{stats["tokens_per_second"]["maximum"]} |\n\n'
        + (
            _resource_statistics_markdown(
                "Cold Run Resource Statistics",
                resource_stats["cold"],
            )
            if resource_stats.get("cold")
            else ""
        )
        + (
            _resource_statistics_markdown(
                "Warm Run Resource Statistics",
                resource_stats["warm"],
            )
            if resource_stats.get("warm")
            else ""
        )
        + "## Individual Runs\n\n"
        "| Run | Type | Total duration | Load duration | "
        "Generated tokens | Generation speed |\n"
        "|---:|---|---:|---:|---:|---:|\n"
        f"{run_rows}\n"
    )

    output_path = output_base.with_suffix(".md")
    output_path.write_text(markdown, encoding="utf-8")

    return output_path


# =============================================================================
# All-prompts master summary reports
# =============================================================================

def write_master_summary_json(
    summary: dict[str, Any],
    output_base: Path,
) -> Path:
    """
    Write the all-prompts master summary as JSON.
    """

    return _write_json(summary, output_base)


def write_master_summary_markdown(
    summary: dict[str, Any],
    output_base: Path,
) -> Path:
    """
    Write the all-prompts master summary as Markdown.
    """

    stats = summary["statistics"]
    think_label = "on" if summary["think_enabled"] else "off"

    prompt_rows = "\n".join(
        "| {prompt} | {runs} | {cold} | {warm} | {duration} s | "
        "{tokens} | {speed} tok/s |".format(
            prompt=prompt["prompt_name"],
            runs=prompt["run_count"],
            cold=prompt["cold_run_count"],
            warm=prompt["warm_run_count"],
            duration=prompt["mean_total_duration_seconds"],
            tokens=prompt["mean_generated_tokens"],
            speed=prompt["mean_tokens_per_second"],
        )
        for prompt in summary["prompts"]
    )

    markdown = (
        "# All-Prompts Benchmark Summary\n\n"
        "## Configuration\n\n"
        "| Item | Value |\n"
        "|---|---|\n"
        f'| Model | `{summary["model"]}` |\n'
        f"| Thinking | `{think_label}` |\n"
        f'| Prompts | `{summary["prompt_count"]}` |\n'
        f'| Total runs | `{summary["total_run_count"]}` |\n'
        f'| Cold runs | `{summary["cold_run_count"]}` |\n'
        f'| Warm runs | `{summary["warm_run_count"]}` |\n\n'
        + _environment_markdown(summary["environment"])
        + "## Overall Statistics\n\n"
        "| Metric | Mean | Median | Minimum | Maximum |\n"
        "|---|---:|---:|---:|---:|\n"
        f'| Total duration (s) | {stats["total_duration_seconds"]["mean"]} | '
        f'{stats["total_duration_seconds"]["median"]} | '
        f'{stats["total_duration_seconds"]["minimum"]} | '
        f'{stats["total_duration_seconds"]["maximum"]} |\n'
        f'| Generated tokens | {stats["generated_tokens"]["mean"]} | '
        f'{stats["generated_tokens"]["median"]} | '
        f'{stats["generated_tokens"]["minimum"]} | '
        f'{stats["generated_tokens"]["maximum"]} |\n'
        f'| Generation speed (tokens/s) | {stats["tokens_per_second"]["mean"]} | '
        f'{stats["tokens_per_second"]["median"]} | '
        f'{stats["tokens_per_second"]["minimum"]} | '
        f'{stats["tokens_per_second"]["maximum"]} |\n\n'
        "## Prompt Results\n\n"
        "| Prompt | Runs | Cold | Warm | Mean total duration | "
        "Mean generated tokens | Mean generation speed |\n"
        "|---|---:|---:|---:|---:|---:|---:|\n"
        f"{prompt_rows}\n"
    )

    output_path = output_base.with_suffix(".md")
    output_path.write_text(markdown, encoding="utf-8")

    return output_path
