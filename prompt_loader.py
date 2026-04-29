"""Load and concatenate editable prompt fragments from prompts/."""

from __future__ import annotations

from pathlib import Path


def prompts_dir() -> Path:
    return Path(__file__).resolve().parent / "prompts"


def load_system_prompt() -> str:
    """All *.md files in prompts/, sorted by name, concatenated."""
    folder = prompts_dir()
    if not folder.is_dir():
        raise FileNotFoundError(f"Missing prompts folder: {folder}")

    parts: list[str] = []
    for path in sorted(folder.glob("*.md")):
        text = path.read_text(encoding="utf-8").strip()
        if text:
            parts.append(text)
    if not parts:
        raise FileNotFoundError(f"No .md files in {folder}")
    return "\n\n---\n\n".join(parts)
