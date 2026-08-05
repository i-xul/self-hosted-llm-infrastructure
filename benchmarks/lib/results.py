"""Benchmark result normalization and summary generation."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from .metrics import (
    calculate_tokens_per_second,
    nanoseconds_to_seconds,
    summarize_numeric_values,
)

CONTEXT_SIZE = 4096
TEMPERATURE = 0
SEED = 42


def build_result_record(
    *,
    result: dict[str, Any],
    prompt_name: str,
    prompt_text: str,
    model: str,
    think_enabled: bool,
    run_type: str,
    run_number: int,
    total_runs: int,
    batch_timestamp: str,
) -> dict[str, Any]:
    """Build the normalized benchmark result record."""
    tokens_per_second = calculate_tokens_per_second(result)

    return {
        "benchmark_timestamp": datetime.now().astimezone().isoformat(),
        "batch_timestamp": batch_timestamp,
        "run_number": run_number,
        "total_runs": total_runs,
        "prompt_name": prompt_name,
        "model": model,
        "think_enabled": think_enabled,
        "run_type": run_type,
        "context_size": CONTEXT_SIZE,
        "temperature": TEMPERATURE,
        "seed": SEED,
        "prompt": prompt_text,
        "response": result.get("response", ""),
        "thinking": result.get("thinking", ""),
        "done_reason": result.get("done_reason"),
        "metrics": {
            "total_duration_seconds": round(
                nanoseconds_to_seconds(result.get("total_duration")), 3
            ),
            "load_duration_seconds": round(
                nanoseconds_to_seconds(result.get("load_duration")), 3
            ),
            "prompt_eval_count": result.get("prompt_eval_count"),
            "prompt_eval_duration_seconds": round(
                nanoseconds_to_seconds(result.get("prompt_eval_duration")), 3
            ),
            "eval_count": result.get("eval_count"),
            "eval_duration_seconds": round(
                nanoseconds_to_seconds(result.get("eval_duration")), 3
            ),
            "tokens_per_second": (
                round(tokens_per_second, 2)
                if tokens_per_second is not None
                else None
            ),
        },
    }


def build_summary_record(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Build aggregate statistics for a repeated benchmark batch."""
    if not records:
        raise ValueError("Cannot build a summary without benchmark records.")

    first = records[0]
    metrics = [record["metrics"] for record in records]

    return {
        "summary_timestamp": datetime.now().astimezone().isoformat(),
        "batch_timestamp": first["batch_timestamp"],
        "model": first["model"],
        "prompt_name": first["prompt_name"],
        "think_enabled": first["think_enabled"],
        "context_size": first["context_size"],
        "temperature": first["temperature"],
        "seed": first["seed"],
        "run_count": len(records),
        "cold_run_count": sum(record["run_type"] == "cold" for record in records),
        "warm_run_count": sum(record["run_type"] == "warm" for record in records),
        "statistics": {
            "total_duration_seconds": summarize_numeric_values(
                [metric["total_duration_seconds"] for metric in metrics]
            ),
            "load_duration_seconds": summarize_numeric_values(
                [metric["load_duration_seconds"] for metric in metrics]
            ),
            "generated_tokens": summarize_numeric_values(
                [metric["eval_count"] for metric in metrics]
            ),
            "generation_duration_seconds": summarize_numeric_values(
                [metric["eval_duration_seconds"] for metric in metrics]
            ),
            "tokens_per_second": summarize_numeric_values(
                [metric["tokens_per_second"] for metric in metrics]
            ),
        },
        "runs": [
            {
                "run_number": record["run_number"],
                "run_type": record["run_type"],
                "total_duration_seconds": record["metrics"]["total_duration_seconds"],
                "load_duration_seconds": record["metrics"]["load_duration_seconds"],
                "generated_tokens": record["metrics"]["eval_count"],
                "generation_duration_seconds": record["metrics"]["eval_duration_seconds"],
                "tokens_per_second": record["metrics"]["tokens_per_second"],
            }
            for record in records
        ],
    }
