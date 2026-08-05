"""Generate the Markdown leaderboard."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def _format_number(
    value: int | float | None,
    *,
    decimals: int = 2,
    suffix: str = "",
) -> str:
    if value is None:
        return "unknown"
    return f"{float(value):.{decimals}f}{suffix}"


def _model_display_name(model_name: str) -> str:
    known_names = {
        "qwen3:8b": "Qwen3 8B",
        "gemma3:12b": "Gemma 3 12B",
    }
    return known_names.get(model_name, model_name)


def _sort_summaries(
    summaries: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return sorted(
        summaries,
        key=lambda item: (
            item.get("average_tokens_per_second") is not None,
            item.get("average_tokens_per_second") or 0,
        ),
        reverse=True,
    )


def build_leaderboard_markdown(
    summaries: list[dict[str, Any]],
) -> str:
    sorted_summaries = _sort_summaries(summaries)

    rows = []
    for rank, summary in enumerate(sorted_summaries, start=1):
        rows.append(
            "| {rank} | {model} | {parameters} | {quantization} | "
            "{speed} | {cold_start} | {date} |".format(
                rank=rank,
                model=_model_display_name(summary["model"]),
                parameters=summary["parameter_size"],
                quantization=summary["quantization"],
                speed=_format_number(
                    summary["average_tokens_per_second"],
                    suffix=" tok/s",
                ),
                cold_start=_format_number(
                    summary["cold_start_seconds"],
                    suffix=" s",
                ),
                date=summary["benchmark_date"],
            )
        )

    metadata_rows = [
        "| {model} | {family} | {source} |".format(
            model=_model_display_name(summary["model"]),
            family=summary["family"],
            source=summary["metadata_source"],
        )
        for summary in sorted_summaries
    ]

    return (
        "# Local LLM Performance Leaderboard\n\n"
        "This leaderboard is generated automatically from the latest "
        "all-prompts master summary for each tested model.\n\n"
        "Models are currently ranked by average token generation speed. "
        "Response quality is evaluated separately in the comparison documents.\n\n"
        "## Performance Ranking\n\n"
        "| Rank | Model | Parameters | Quantization | "
        "Average generation speed | Cold start | Benchmark date |\n"
        "|---:|---|---:|---|---:|---:|---|\n"
        + "\n".join(rows)
        + "\n\n"
        "## Metadata Sources\n\n"
        "| Model | Family | Metadata source |\n"
        "|---|---|---|\n"
        + "\n".join(metadata_rows)
        + "\n\n"
        "## Interpretation\n\n"
        "- Average generation speed is calculated across the full "
        "all-prompts benchmark pass.\n"
        "- Cold start includes loading the model from local storage.\n"
        "- All current models use Q4_K_M quantization and were tested "
        "with GPU acceleration.\n"
        "- A higher token rate does not automatically indicate better "
        "response quality.\n"
        "- Manual quality comparisons are stored in "
        "`benchmarks/comparisons/`.\n"
    )


def write_leaderboard(
    *,
    summaries: list[dict[str, Any]],
    output_path: Path,
) -> Path:
    output_path.write_text(
        build_leaderboard_markdown(summaries),
        encoding="utf-8",
    )
    return output_path
