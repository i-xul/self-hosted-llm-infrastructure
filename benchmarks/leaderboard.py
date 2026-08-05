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
# Version: v0.5.0
#
# Purpose:
# Generate a Markdown leaderboard from benchmark and quality data.
#
# Workflow:
# 1. Load benchmark summaries.\n# 2. Load quality scores.\n# 3. Generate LEADERBOARD.md.
#
# ----------------------------------------------------------------------

"""Command-line entry point for leaderboard generation."""

from pathlib import Path

from leaderboard.loader import load_latest_model_summaries
from leaderboard.markdown import write_leaderboard
from leaderboard.quality import load_quality_scores

# =============================================================================
# Generated output path
# =============================================================================

OUTPUT_PATH = Path(__file__).resolve().parent / "LEADERBOARD.md"


# =============================================================================
# Main workflow
# =============================================================================

def main() -> None:
    """Load benchmark and quality data, then write LEADERBOARD.md."""
    summaries = load_latest_model_summaries()

    if not summaries:
        print("No benchmark summaries were found.")
        return

    quality_data = load_quality_scores()
    output_path = write_leaderboard(
        summaries=summaries,
        quality_data=quality_data,
        output_path=OUTPUT_PATH,
    )

    print(f"Loaded model summaries: {len(summaries)}")
    print(f"Loaded quality evaluations: {len(quality_data['models'])}")
    print(f"Leaderboard written to: {output_path}")


if __name__ == "__main__":
    main()
