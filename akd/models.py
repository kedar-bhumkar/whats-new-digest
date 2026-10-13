from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal

DIMENSIONS = ("significance", "relevance", "actionability", "novelty")


@dataclass(frozen=True)
class Item:
    id: str
    source: str
    title: str
    url: str
    text: str
    published_at: datetime


@dataclass
class Scored:
    item: Item
    category: str
    scores: dict[str, float]  # keys: DIMENSIONS, each normalized 0..1
    hype_p: float
    confidence: float
    rank: float = 0.0
    low_confidence: bool = False


@dataclass
class Selected:
    scored: Scored
    tier: Literal["pick", "notable"]
    why: str = field(default="")
