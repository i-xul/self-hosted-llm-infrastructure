"""Benchmark metric calculations."""

from __future__ import annotations

from typing import Any


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
