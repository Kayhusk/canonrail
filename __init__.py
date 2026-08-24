"""Hermes adapter for CanonRail."""

from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
SKILL = ROOT / "skills" / "canonrail" / "SKILL.md"


def register(ctx: Any) -> None:
    """Register the portable CanonRail skill."""
    ctx.register_skill("canonrail", SKILL)
