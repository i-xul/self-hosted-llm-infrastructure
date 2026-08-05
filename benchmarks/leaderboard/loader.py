"""Load and normalize benchmark master-summary files."""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"

MODEL_METADATA_OVERRIDES: dict[str, dict[str, str]] = {
    "qwen3:8b": {
        "family": "qwen3",
        "parameter_size": "8.2B",
        "quantization": "Q4_K_M",
    },
}


def find_master_summaries() -> list[Path]:
    if not RESULTS_DIR.exists():
        return []
    return sorted(RESULTS_DIR.rglob("*_master-summary.json"))


def find_latest_summary_per_model() -> list[Path]:
    newest_by_model: dict[str, Path] = {}

    for path in find_master_summaries():
        model_directory = path.parent.name
        current = newest_by_model.get(model_directory)

        if current is None or path.stat().st_mtime > current.stat().st_mtime:
            newest_by_model[model_directory] = path

    return sorted(
        newest_by_model.values(),
        key=lambda path: path.parent.name.casefold(),
    )


def read_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON file: {path}") from error

    if not isinstance(data, dict):
        raise ValueError(f"Expected a JSON object in: {path}")

    return data


def _extract_cold_start_seconds(data: dict[str, Any]) -> float | None:
    for prompt in data.get("prompts", []):
        if prompt.get("cold_run_count", 0) > 0:
            value = prompt.get("mean_total_duration_seconds")
            if value is not None:
                return float(value)
    return None


def _extract_benchmark_date(data: dict[str, Any]) -> str:
    timestamp = data.get("summary_timestamp")

    if not timestamp:
        return "unknown"

    try:
        return datetime.fromisoformat(timestamp).date().isoformat()
    except ValueError:
        return str(timestamp)


def _infer_family(model_name: str) -> str:
    base_name = model_name.split(":", maxsplit=1)[0]
    lowered = base_name.casefold()

    for prefix, family in (
        ("qwen", "qwen"),
        ("gemma", "gemma"),
        ("llama", "llama"),
        ("mistral", "mistral"),
        ("phi", "phi"),
        ("deepseek", "deepseek"),
    ):
        if lowered.startswith(prefix):
            return family

    return base_name or "unknown"


def _infer_parameter_size(model_name: str) -> str:
    match = re.search(
        r"(?::|[-_])(?P<size>\d+(?:\.\d+)?)(?P<unit>[bBmM])(?:$|[-_])",
        model_name,
    )

    if not match:
        return "unknown"

    return f"{match.group('size')}{match.group('unit').upper()}"


def _resolve_model_metadata(
    model_name: str,
    model_metadata: dict[str, Any],
) -> dict[str, str]:
    override = MODEL_METADATA_OVERRIDES.get(model_name, {})

    family = (
        model_metadata.get("family")
        or override.get("family")
        or _infer_family(model_name)
    )
    parameter_size = (
        model_metadata.get("parameter_size")
        or override.get("parameter_size")
        or _infer_parameter_size(model_name)
    )
    quantization = (
        model_metadata.get("quantization_level")
        or override.get("quantization")
        or "unknown"
    )

    if (
        model_metadata.get("family")
        and model_metadata.get("parameter_size")
        and model_metadata.get("quantization_level")
    ):
        metadata_source = "benchmark metadata"
    elif override:
        metadata_source = "compatibility override"
    else:
        metadata_source = "model-name inference"

    return {
        "family": str(family),
        "parameter_size": str(parameter_size),
        "quantization": str(quantization),
        "metadata_source": metadata_source,
    }


def normalize_summary(
    data: dict[str, Any],
    source_path: Path,
) -> dict[str, Any]:
    model_name = str(data.get("model", source_path.parent.name))
    environment = data.get("environment", {})
    model_metadata = environment.get("model", {})
    statistics = data.get("statistics", {})
    speed_stats = statistics.get("tokens_per_second", {})

    resolved = _resolve_model_metadata(model_name, model_metadata)

    return {
        "model": model_name,
        "family": resolved["family"],
        "parameter_size": resolved["parameter_size"],
        "quantization": resolved["quantization"],
        "metadata_source": resolved["metadata_source"],
        "average_tokens_per_second": speed_stats.get("mean"),
        "cold_start_seconds": _extract_cold_start_seconds(data),
        "benchmark_date": _extract_benchmark_date(data),
        "source_path": str(source_path),
    }


def load_latest_model_summaries() -> list[dict[str, Any]]:
    return [
        normalize_summary(read_json(path), path)
        for path in find_latest_summary_per_model()
    ]
