"""Benchmark result normalization."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from .metrics import calculate_tokens_per_second, nanoseconds_to_seconds

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
) -> dict[str, Any]:
    """Build the normalized benchmark result record."""
    tokens_per_second = calculate_tokens_per_second(result)

    return {
        "benchmark_timestamp": datetime.now().astimezone().isoformat(),
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
