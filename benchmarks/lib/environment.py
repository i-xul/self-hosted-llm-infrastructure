#!/usr/bin/env python3
#
# ----------------------------------------------------------------------
# Self-Hosted LLM Infrastructure
# ----------------------------------------------------------------------
#
# Author: H A (i-xul)
# Repository: https://github.com/i-xul/self-hosted-llm-infrastructure
#
# File: benchmarks/lib/environment.py
# Created: 2026-08-05
# Version: v1.0.0
#
# Purpose:
# Collects operating-system, Python, Ollama, and model metadata for
# reproducible benchmark reports.
#
# Workflow:
# 1. Read local operating-system and Python information.
# 2. Query Ollama version information.
# 3. Query installed model metadata.
# 4. Normalize the collected environment record.
#
# ----------------------------------------------------------------------

"""Collect benchmark environment and model metadata."""

from __future__ import annotations

import platform
import sys
from typing import Any

from .api import get_model_details, get_ollama_version


# =============================================================================
# Environment metadata collection
# =============================================================================

def collect_environment_metadata(
    *,
    generate_api_url: str,
    model: str,
    timeout: int,
) -> dict[str, Any]:
    """
    Collect stable software, operating-system, and model metadata.

    The returned object is embedded in benchmark result and summary reports.
    """

    version_data = get_ollama_version(
        generate_api_url=generate_api_url,
        timeout=timeout,
    )

    model_data = get_model_details(
        generate_api_url=generate_api_url,
        model=model,
        timeout=timeout,
    )

    details = model_data.get("details", {})
    model_info = model_data.get("model_info", {})

    context_length = None

    for key, value in model_info.items():
        if key.endswith(".context_length"):
            context_length = value
            break

    return {
        "operating_system": platform.platform(),
        "python_version": sys.version.split()[0],
        "python_implementation": platform.python_implementation(),
        "machine_architecture": platform.machine(),
        "ollama_version": version_data.get("version"),
        "model": {
            "name": model,
            "format": details.get("format"),
            "family": details.get("family"),
            "families": details.get("families", []),
            "parameter_size": details.get("parameter_size"),
            "quantization_level": details.get("quantization_level"),
            "context_length": context_length,
        },
    }
