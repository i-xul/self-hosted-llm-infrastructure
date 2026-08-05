"""Benchmark prompt loading and validation."""

from __future__ import annotations

from pathlib import Path

from .utils import PROMPTS_DIR


def resolve_prompt_path(prompt_name: str) -> Path:
    """Resolve a prompt name to a Markdown file in the prompts directory."""
    candidate = Path(prompt_name)

    if candidate.suffix.lower() != ".md":
        candidate = candidate.with_suffix(".md")

    prompt_path = PROMPTS_DIR / candidate.name

    if not prompt_path.is_file():
        available = ", ".join(
            sorted(path.name for path in PROMPTS_DIR.glob("*.md"))
        )
        raise FileNotFoundError(
            f"Prompt not found: {prompt_path}\n"
            f"Available prompts: {available or 'none'}"
        )

    return prompt_path


def read_prompt(prompt_path: Path) -> str:
    """Read and validate a benchmark prompt."""
    prompt = prompt_path.read_text(encoding="utf-8").strip()

    if not prompt:
        raise ValueError(f"Prompt file is empty: {prompt_path}")

    return prompt
