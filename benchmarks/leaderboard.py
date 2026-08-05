#!/usr/bin/env python3
#
# ----------------------------------------------------------------------
# Self-Hosted LLM Infrastructure
# ----------------------------------------------------------------------
#
# Author: H A (i-xul)
# Repository: https://github.com/i-xul/self-hosted-llm-infrastructure
#
# File: benchmarks/leaderboard.py
# Created: 2026-08-05
# Version: v0.4.0
#
# Purpose:
# Generates an automatically updated Markdown leaderboard from the
# latest all-prompts benchmark summary for every tested model.
#
# Workflow:
# 1. Load and normalize the newest summary for each model.
# 2. Rank models by measured generation speed.
# 3. Generate benchmarks/LEADERBOARD.md.
#
# ----------------------------------------------------------------------

"""Command-line entry point for Markdown leaderboard generation."""

from pathlib import Path

from leaderboard.loader import load_latest_model_summaries
from leaderboard.markdown import write_leaderboard


# =============================================================================
# Generated leaderboard path
# =============================================================================

OUTPUT_PATH = Path(__file__).resolve().parent / "LEADERBOARD.md"


# =============================================================================
# Main leaderboard workflow
# =============================================================================

def main() -> None:
    """
    Load current benchmark summaries and generate LEADERBOARD.md.
    """

    summaries = load_latest_model_summaries()

    if not summaries:
        print("No benchmark summaries were found.")
        return

    output_path = write_leaderboard(
        summaries=summaries,
        output_path=OUTPUT_PATH,
    )

    print(f"Loaded model summaries: {len(summaries)}")
    print(f"Leaderboard written to: {output_path}")


if __name__ == "__main__":
    main()
