from __future__ import annotations

from dataclasses import dataclass, field
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
    youtube_channels: list[dict] = field(default_factory=list)
    x_handles: list[str] = field(default_factory=list)
    x_searches: list[str] = field(default_factory=list)
    x_min_likes: int = 50
    x_max_items: int = 150


def load_config(path: Path) -> Config:
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    weights = {k: float(v) for k, v in raw["weights"].items()}
    if set(weights) != set(DIMENSIONS):
        raise ValueError(f"weights must cover exactly {DIMENSIONS}")
    if abs(sum(weights.values()) - 1.0) > 1e-9:
        raise ValueError("weights must sum to 1.0")
    x = raw.get("x") or {}
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
        x_handles=[str(h).lstrip("@") for h in x.get("handles") or []],
        x_searches=[str(t) for t in x.get("searches") or []],
        x_min_likes=int(x.get("min_likes", 50)),
        x_max_items=int(x.get("max_items", 150)),
        youtube_channels=[{"id": str(c["id"]), "name": str(c.get("name", c["id"]))} for c in raw.get("youtube_channels") or []],
    )


def load_profile(path: Path) -> str:
    """The profile is passed to Jev verbatim as state, so return it as text."""
    return Path(path).read_text(encoding="utf-8")
