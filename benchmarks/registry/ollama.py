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
# Version: v0.2.0
#
# Purpose:
# Read the models currently installed in the local Ollama
# environment by parsing the ollama list command output.
#
# Workflow:
# 1. Run ollama list without invoking a shell.
# 2. Validate successful command execution.
# 3. Parse installed model names, IDs, and sizes.
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

    Raises:
        RuntimeError: If Ollama is unavailable or the command fails.
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
# Ollama list output parsing
# =============================================================================

def parse_ollama_list(output: str) -> list[dict[str, Any]]:
    """
    Parse model records from ollama list terminal output.

    The parser treats the first whitespace-separated column as the model name,
    the second as the model ID, and combines the next two columns as the size.

    Args:
        output: Raw standard output from ollama list.

    Returns:
        Installed model records sorted by model name.
    """

    lines = [
        line.strip()
        for line in output.splitlines()
        if line.strip()
    ]

    if not lines:
        return []

    data_lines = lines[1:]
    models: list[dict[str, Any]] = []

    for line in data_lines:
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
    Return models currently installed in the local Ollama environment.
    """

    return parse_ollama_list(_run_ollama_list())
