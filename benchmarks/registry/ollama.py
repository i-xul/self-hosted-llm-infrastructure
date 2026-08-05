#!/usr/bin/env python3
#
# ----------------------------------------------------------------------
# Self-Hosted LLM Infrastructure
# ----------------------------------------------------------------------
#
# Author: H A (i-xul)
# Repository: https://github.com/i-xul/self-hosted-llm-infrastructure
#
# File: benchmarks/registry/ollama.py
# Created: 2026-08-06
# Version: v0.3.0
#
# Purpose:
# Read models currently installed in the local Ollama environment.
#
# Workflow:
# 1. Run ollama list.
# 2. Validate command execution.
# 3. Parse model name, ID, and size.
# 4. Return normalized installed-model records.
#
# ----------------------------------------------------------------------

"""Read installed models from the local Ollama command-line client."""

from __future__ import annotations

import subprocess
from typing import Any


# =============================================================================
# Ollama command execution
# =============================================================================

def _run_ollama_list() -> str:
    """
    Run ollama list and return its standard output.
    """

    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError as error:
        raise RuntimeError(
            "The ollama command was not found in PATH."
        ) from error

    if result.returncode != 0:
        details = result.stderr.strip() or "Unknown Ollama error."

        raise RuntimeError(
            f"ollama list failed with exit code "
            f"{result.returncode}: {details}"
        )

    return result.stdout


# =============================================================================
# Ollama list parsing
# =============================================================================

def parse_ollama_list(output: str) -> list[dict[str, Any]]:
    """
    Parse installed model records from ollama list output.
    """

    lines = [
        line.strip()
        for line in output.splitlines()
        if line.strip()
    ]

    if not lines:
        return []

    models: list[dict[str, Any]] = []

    for line in lines[1:]:
        parts = line.split()

        if len(parts) < 4:
            raise RuntimeError(
                f"Unexpected ollama list output line: {line}"
            )

        models.append(
            {
                "name": parts[0],
                "id": parts[1],
                "size": f"{parts[2]} {parts[3]}",
            }
        )

    return sorted(
        models,
        key=lambda model: model["name"].casefold(),
    )


def load_installed_models() -> list[dict[str, Any]]:
    """
    Return models currently installed in Ollama.
    """

    return parse_ollama_list(_run_ollama_list())
