#!/usr/bin/env python3
#
# ----------------------------------------------------------------------
# Self-Hosted LLM Infrastructure
# ----------------------------------------------------------------------
#
# Author: H A (i-xul)
# Repository: https://github.com/i-xul/self-hosted-llm-infrastructure
#
# File: benchmarks/leaderboard/quality.py
# Created: 2026-08-05
# Version: v0.5.0
#
# Purpose:
# Load, validate, and normalize manual model quality scores.
#
# Workflow:
# 1. Read quality_scores.json.\n# 2. Validate the score scale.\n# 3. Calculate overall scores.
#
# ----------------------------------------------------------------------

"""Manual model quality score loading and validation."""

from __future__ import annotations

import json
from pathlib import Path
from statistics import mean
from typing import Any

# =============================================================================
# Quality score file
# =============================================================================

QUALITY_SCORES_PATH = (
    Path(__file__).resolve().parent.parent
    / "quality"
    / "quality_scores.json"
)


# =============================================================================
# Loading and validation
# =============================================================================

def _read_json(path: Path) -> dict[str, Any]:
    """Read the quality score JSON object."""
    if not path.is_file():
        return {
            "schema_version": 1,
            "scoring_scale": {"minimum": 1, "maximum": 10, "step": 0.5},
            "evaluation_scope": "No quality score file found.",
            "models": {},
        }

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid quality score JSON: {path}") from error

    if not isinstance(data, dict):
        raise ValueError(f"Expected a JSON object in: {path}")

    return data


def _validate_score(
    *,
    model_name: str,
    category: str,
    value: Any,
    minimum: float,
    maximum: float,
    step: float,
) -> float:
    """Validate one score against the configured range and step."""
    if not isinstance(value, (int, float)):
        raise ValueError(f"Non-numeric score: {model_name}/{category}")

    score = float(value)

    if not minimum <= score <= maximum:
        raise ValueError(f"Score outside range: {model_name}/{category}")

    units = round((score - minimum) / step)

    if abs(minimum + units * step - score) > 1e-9:
        raise ValueError(f"Invalid score step: {model_name}/{category}")

    return score


def load_quality_scores(
    path: Path = QUALITY_SCORES_PATH,
) -> dict[str, Any]:
    """Load quality evaluations and calculate overall model scores."""
    data = _read_json(path)
    scale = data.get("scoring_scale", {})
    minimum = float(scale.get("minimum", 1))
    maximum = float(scale.get("maximum", 10))
    step = float(scale.get("step", 0.5))

    if step <= 0:
        raise ValueError("Quality score step must be greater than zero.")

    raw_models = data.get("models", {})

    if not isinstance(raw_models, dict):
        raise ValueError("Quality score models must be a JSON object.")

    models: dict[str, dict[str, Any]] = {}

    for model_name, model_data in raw_models.items():
        raw_scores = model_data.get("scores", {})
        scores = {
            category: _validate_score(
                model_name=model_name,
                category=category,
                value=value,
                minimum=minimum,
                maximum=maximum,
                step=step,
            )
            for category, value in raw_scores.items()
        }

        models[model_name] = {
            "display_name": model_data.get("display_name", model_name),
            "scores": scores,
            "notes": model_data.get("notes", {}),
            "overall_score": round(mean(scores.values()), 2) if scores else None,
        }

    return {
        "schema_version": data.get("schema_version", 1),
        "scoring_scale": {
            "minimum": minimum,
            "maximum": maximum,
            "step": step,
        },
        "evaluation_scope": data.get(
            "evaluation_scope",
            "Manual benchmark response evaluation",
        ),
        "models": models,
    }
