#!/usr/bin/env python3
#
# ----------------------------------------------------------------------
# Self-Hosted LLM Infrastructure
# ----------------------------------------------------------------------
#
# Author: H A (i-xul)
# Repository: https://github.com/i-xul/self-hosted-llm-infrastructure
#
# File: benchmarks/lib/prompts.py
# Created: 2026-08-05
# Version: v1.0.0
#
# Purpose:
# Locates, validates, and reads version-controlled benchmark prompts.
#
# Workflow:
# 1. List available Markdown prompts.
# 2. Resolve a prompt name to a safe local path.
# 3. Read and validate prompt content.
#
# ----------------------------------------------------------------------

"""Benchmark prompt loading and validation."""

from __future__ import annotations

from pathlib import Path

from .utils import PROMPTS_DIR


# =============================================================================
# Prompt discovery
# =============================================================================

def list_prompt_paths() -> list[Path]:
    """
    Return every Markdown prompt in deterministic filename order.
    """

    return sorted(
        PROMPTS_DIR.glob("*.md"),
        key=lambda path: path.name.casefold(),
    )


def resolve_prompt_path(prompt_name: str | None) -> Path:
    """
    Resolve a prompt name to a Markdown file in the prompts directory.
    """

    if not prompt_name:
        raise ValueError("A prompt name is required.")

    candidate = Path(prompt_name)

    if candidate.suffix.lower() != ".md":
        candidate = candidate.with_suffix(".md")

    prompt_path = PROMPTS_DIR / candidate.name

    if not prompt_path.is_file():
        available = ", ".join(path.name for path in list_prompt_paths())

        raise FileNotFoundError(
            f"Prompt not found: {prompt_path}\n"
            f"Available prompts: {available or 'none'}"
        )

    return prompt_path


# =============================================================================
# Prompt content loading
# =============================================================================

def read_prompt(prompt_path: Path) -> str:
    """
    Read one prompt file and reject empty prompt content.
    """

    prompt = prompt_path.read_text(encoding="utf-8").strip()

    if not prompt:
        raise ValueError(f"Prompt file is empty: {prompt_path}")

    return prompt
