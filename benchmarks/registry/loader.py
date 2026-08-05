#!/usr/bin/env python3
#
# ----------------------------------------------------------------------
# Self-Hosted LLM Infrastructure
# ----------------------------------------------------------------------
#
# Author: H A (i-xul)
# Repository: https://github.com/i-xul/self-hosted-llm-infrastructure
#
# File: benchmarks/registry/loader.py
# Created: 2026-08-06
# Version: v0.3.0
#
# Purpose:
# Load and validate persistent model metadata from models.json.
#
# Workflow:
# 1. Locate models.json.
# 2. Read and decode JSON.
# 3. Validate required persistent model fields.
# 4. Return a normalized registry object.
#
# ----------------------------------------------------------------------

"""Load and validate persistent model registry metadata."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


# =============================================================================
# Registry file location
# =============================================================================

REGISTRY_PATH = Path(__file__).resolve().parent / "models.json"


# =============================================================================
# JSON loading
# =============================================================================

def _read_json(path: Path) -> dict[str, Any]:
    """
    Read and decode the registry JSON file.
    """

    if not path.is_file():
        raise FileNotFoundError(f"Registry file not found: {path}")

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid registry JSON: {path}") from error

    if not isinstance(data, dict):
        raise ValueError("Registry root must be a JSON object.")

    return data


# =============================================================================
# Model entry validation
# =============================================================================

def _normalize_model(
    model: Any,
    *,
    index: int,
) -> dict[str, str]:
    """
    Validate one persistent model metadata entry.
    """

    if not isinstance(model, dict):
        raise ValueError(f"Model entry {index} must be a JSON object.")

    normalized: dict[str, str] = {}

    for field in ("name", "display_name", "family"):
        value = model.get(field)

        if not isinstance(value, str) or not value.strip():
            raise ValueError(
                f"Model entry {index} has invalid field: {field}"
            )

        normalized[field] = value.strip()

    return normalized


# =============================================================================
# Complete registry loading
# =============================================================================

def load_registry(
    path: Path = REGISTRY_PATH,
) -> dict[str, Any]:
    """
    Load and normalize the complete persistent model registry.
    """

    data = _read_json(path)
    schema_version = data.get("schema_version")

    if not isinstance(schema_version, int) or schema_version < 1:
        raise ValueError("Registry schema_version must be a positive integer.")

    raw_models = data.get("models")

    if not isinstance(raw_models, list):
        raise ValueError("Registry models field must be a JSON array.")

    models = [
        _normalize_model(model, index=index)
        for index, model in enumerate(raw_models)
    ]

    model_names = [model["name"] for model in models]

    if len(model_names) != len(set(model_names)):
        raise ValueError("Registry contains duplicate model names.")

    return {
        "schema_version": schema_version,
        "models": models,
    }
