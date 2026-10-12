from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from akd.models import DIMENSIONS


@dataclass(frozen=True)
class Config:
    weights: dict[str, float]
    max_picks: int
    max_notable: int
    min_notable_rank: float
    hype_penalty: float
    low_confidence_threshold: float
    window_days: int
    max_age_days: int
    subreddits: list[str]
    feeds: list[str]
    github_topics: list[str]
    github_watchlist: list[str]


def load_config(path: Path) -> Config:
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    weights = {k: float(v) for k, v in raw["weights"].items()}
    if set(weights) != set(DIMENSIONS):
        raise ValueError(f"weights must cover exactly {DIMENSIONS}")
    if abs(sum(weights.values()) - 1.0) > 1e-9:
        raise ValueError("weights must sum to 1.0")
    return Config(
        weights=weights,
        max_picks=int(raw["max_picks"]),
        max_notable=int(raw["max_notable"]),
        min_notable_rank=float(raw["min_notable_rank"]),
        hype_penalty=float(raw["hype_penalty"]),
        low_confidence_threshold=float(raw["low_confidence_threshold"]),
        window_days=int(raw["window_days"]),
        max_age_days=int(raw.get("max_age_days", 3)),
        subreddits=list(raw.get("subreddits", [])),
        feeds=list(raw.get("feeds", [])),
        github_topics=list(raw.get("github_topics", [])),
        github_watchlist=list(raw.get("github_watchlist", [])),
    )


def load_profile(path: Path) -> str:
    """The profile is passed to Jev verbatim as state, so return it as text."""
    return Path(path).read_text(encoding="utf-8")
