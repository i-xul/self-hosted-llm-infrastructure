#!/usr/bin/env python3
#
# ----------------------------------------------------------------------
# Self-Hosted LLM Infrastructure
# ----------------------------------------------------------------------
#
# Author: H A (i-xul)
# Repository: https://github.com/i-xul/self-hosted-llm-infrastructure
#
# File: benchmarks/leaderboard/markdown.py
# Created: 2026-08-05
# Version: v0.5.0
#
# Purpose:
# Generate separate performance and manual quality rankings.
#
# Workflow:
# 1. Format values.\n# 2. Rank performance.\n# 3. Rank quality.\n# 4. Write LEADERBOARD.md.
#
# ----------------------------------------------------------------------

"""Markdown leaderboard generation."""

from __future__ import annotations

from pathlib import Path
from typing import Any

# =============================================================================
# Formatting helpers
# =============================================================================

def _format_number(
    value: int | float | None,
    *,
    decimals: int = 2,
    suffix: str = "",
) -> str:
    """Format an optional numeric benchmark value."""
    return "unknown" if value is None else f"{float(value):.{decimals}f}{suffix}"


def _format_score(value: int | float | None) -> str:
    """Format an optional quality score."""
    return "not rated" if value is None else f"{float(value):.1f}/10"


def _display_name(
    model_name: str,
    quality_models: dict[str, dict[str, Any]],
) -> str:
    """Return the configured model display name."""
    return str(
        quality_models.get(model_name, {}).get("display_name", model_name)
    )


# =============================================================================
# Ranking helpers
# =============================================================================

def _sort_by_speed(
    summaries: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Sort models by average generation speed."""
    return sorted(
        summaries,
        key=lambda item: item.get("average_tokens_per_second") or 0,
        reverse=True,
    )


def _sort_by_quality(
    summaries: list[dict[str, Any]],
    quality_models: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    """Sort benchmarked models by overall manual quality score."""
    return sorted(
        summaries,
        key=lambda item: quality_models.get(
            item["model"], {}
        ).get("overall_score") or 0,
        reverse=True,
    )


# =============================================================================
# Markdown document generation
# =============================================================================

def build_leaderboard_markdown(
    *,
    summaries: list[dict[str, Any]],
    quality_data: dict[str, Any],
) -> str:
    """Build the combined performance and quality leaderboard."""
    quality_models = quality_data.get("models", {})
    scale = quality_data.get("scoring_scale", {})

    performance_rows = []
    for rank, summary in enumerate(_sort_by_speed(summaries), start=1):
        performance_rows.append(
            "| {rank} | {model} | {parameters} | {quantization} | "
            "{speed} | {cold} | {date} |".format(
                rank=rank,
                model=_display_name(summary["model"], quality_models),
                parameters=summary["parameter_size"],
                quantization=summary["quantization"],
                speed=_format_number(
                    summary["average_tokens_per_second"],
                    suffix=" tok/s",
                ),
                cold=_format_number(
                    summary["cold_start_seconds"],
                    suffix=" s",
                ),
                date=summary["benchmark_date"],
            )
        )

    quality_rows = []
    for rank, summary in enumerate(
        _sort_by_quality(summaries, quality_models),
        start=1,
    ):
        model_quality = quality_models.get(summary["model"], {})
        scores = model_quality.get("scores", {})

        quality_rows.append(
            "| {rank} | {model} | {finnish} | {python} | "
            "{summary_score} | {overall} |".format(
                rank=rank,
                model=_display_name(summary["model"], quality_models),
                finnish=_format_score(scores.get("finnish")),
                python=_format_score(scores.get("python")),
                summary_score=_format_score(scores.get("summarization")),
                overall=_format_score(model_quality.get("overall_score")),
            )
        )

    metadata_rows = [
        "| {model} | {family} | {source} |".format(
            model=_display_name(summary["model"], quality_models),
            family=summary["family"],
            source=summary["metadata_source"],
        )
        for summary in _sort_by_speed(summaries)
    ]

    return (
        "# Local LLM Performance and Quality Leaderboard\n\n"
        "Performance and manually evaluated response quality are ranked "
        "separately because faster generation does not guarantee better answers.\n\n"
        "## Performance Ranking\n\n"
        "| Rank | Model | Parameters | Quantization | "
        "Average generation speed | Cold start | Benchmark date |\n"
        "|---:|---|---:|---|---:|---:|---|\n"
        + "\n".join(performance_rows)
        + "\n\n"
        "## Manual Quality Ranking\n\n"
        "| Rank | Model | Finnish | Python | Summarization | Overall |\n"
        "|---:|---|---:|---:|---:|---:|\n"
        + "\n".join(quality_rows)
        + "\n\n"
        f"Quality scale: {scale.get('minimum', 1)}–"
        f"{scale.get('maximum', 10)}, step {scale.get('step', 0.5)}.\n\n"
        f"**Evaluation scope:** {quality_data.get('evaluation_scope')}\n\n"
        "## Metadata Sources\n\n"
        "| Model | Family | Metadata source |\n"
        "|---|---|---|\n"
        + "\n".join(metadata_rows)
        + "\n\n"
        "## Interpretation\n\n"
        "- Performance values come from each model's latest all-prompts run.\n"
        "- Cold start includes model loading from local storage.\n"
        "- Overall quality is the arithmetic mean of available category scores.\n"
        "- Manual scores are preliminary human evaluations, not objective facts.\n"
        "\n"
        "## Quality Comparisons\n\n"
        "Performance metrics should be interpreted together with manual "
        "response-quality evaluations.\n\n"
        "- [Four-model comparison: Qwen3 8B vs. Gemma 3 12B vs. Llama 3.1 8B vs. Phi-4 14B]"
        "(comparisons/qwen3-vs-gemma3-vs-llama3.1-vs-phi4.md)\n"
        "- [Earlier comparison: Qwen3 8B vs. Gemma 3 12B]"
        "(comparisons/qwen3-8b-vs-gemma3-12b.md)\n"
    )


def write_leaderboard(
    *,
    summaries: list[dict[str, Any]],
    quality_data: dict[str, Any],
    output_path: Path,
) -> Path:
    """Write the generated leaderboard to disk."""
    output_path.write_text(
        build_leaderboard_markdown(
            summaries=summaries,
            quality_data=quality_data,
        ),
        encoding="utf-8",
    )
    return output_path
