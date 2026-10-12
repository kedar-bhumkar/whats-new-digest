"""Publisher: merge a day's selection into items.json (site) and whats-new.md (digest).

Everything is built and validated in memory first; nothing is written unless the JSON
validates. AKD owns only its own `## YYYY-MM-DD (AKD)` markdown section, so the old
routine's same-day section is never touched.
"""

from __future__ import annotations

import json
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlsplit

import jsonschema

from akd.collectors.base import strip_html
from akd.models import Selected

SCHEMA_PATH = Path(__file__).parent / "schema" / "items.schema.json"
ITEMS_RELPATH = Path("public") / "whats-new" / "items.json"
MD_NAME = "whats-new.md"
MD_HEADER = "# What's New Digest\n\n"


def validate(doc: dict) -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    jsonschema.validate(doc, schema)


def _item_dict(sel: Selected) -> dict | None:
    s = sel.scored
    parts = urlsplit(s.item.url)
    if parts.scheme not in ("http", "https") or not parts.netloc:
        return None  # javascript:, data:, etc. never reach the site
    title = strip_html(s.item.title) or s.item.url
    return {
        "id": s.item.id,
        "title": title,
        "url": s.item.url,
        "source": s.item.source,
        "category": s.category,
        "why": strip_html(sel.why),
        "rank": round(s.rank, 4),
        "scores": {k: round(v, 4) for k, v in s.scores.items()},
        "flags": {"low_confidence": s.low_confidence, "hype_p": round(s.hype_p, 4)},
    }


def _tier(selected: list[Selected], tier: str) -> list[dict]:
    return [d for sel in selected if sel.tier == tier and (d := _item_dict(sel)) is not None]


def merge_day(
    existing: dict, day: date, selected: list[Selected], window_days: int, now: datetime | None = None
) -> dict:
    """Replace `day`'s block, trim to the window (relative to the newest day), newest first."""
    now = now or datetime.now(timezone.utc)
    block = {"date": day.isoformat(), "picks": _tier(selected, "pick"), "notable": _tier(selected, "notable")}
    days = [d for d in existing.get("days", []) if d["date"] != block["date"]] + [block]
    newest = max(date.fromisoformat(d["date"]) for d in days)
    cutoff = (newest - timedelta(days=window_days)).isoformat()
    days = sorted((d for d in days if d["date"] >= cutoff), key=lambda d: d["date"], reverse=True)
    return {"lastUpdated": now.isoformat(), "days": days}


def _md_section(day: date, selected: list[Selected]) -> str:
    blocks = []
    for sel in selected:
        d = _item_dict(sel)
        if d is None:
            continue
        label = "Top pick" if sel.tier == "pick" else "Notable"
        why = f" - {d['why']}" if d["why"] else ""
        blocks.append(f"- **{d['title']}** ({label}; {d['category']}; {d['source']}){why}\n  - Link: {d['url']}\n")
    return f"## {day.isoformat()} (AKD)\n\n" + "\n".join(blocks) + "\n"


def prepend_markdown(md: str, day: date, selected: list[Selected]) -> str:
    crlf = "\r\n" in md
    text = md.replace("\r\n", "\n")
    section = _md_section(day, selected)
    own = re.compile(rf"^## {re.escape(day.isoformat())} \(AKD\)\n.*?(?=^## |\Z)", re.M | re.S)
    if own.search(text):
        out = own.sub(lambda _: section, text, count=1)
    else:
        first = re.search(r"^## ", text, re.M)
        if first:
            out = text[: first.start()] + section + text[first.start() :]
        else:
            out = text + ("" if not text or text.endswith("\n\n") else "\n") + section
    return out.replace("\n", "\r\n") if crlf else out


def write_outputs(
    selected: list[Selected],
    day: date,
    digest_dir: Path,
    site_dir: Path,
    window_days: int = 60,
    now: datetime | None = None,
) -> None:
    """Write items.json under `site_dir` and whats-new.md under `digest_dir`.

    No-op for an empty selection. Raises jsonschema.ValidationError before writing anything
    if the resulting JSON is invalid.
    """
    if not selected:
        return
    items_path = Path(site_dir) / ITEMS_RELPATH
    existing = json.loads(items_path.read_text(encoding="utf-8")) if items_path.exists() else {}
    doc = merge_day(existing, day, selected, window_days, now)
    validate(doc)

    md_path = Path(digest_dir) / MD_NAME
    md = md_path.read_bytes().decode("utf-8") if md_path.exists() else MD_HEADER
    new_md = prepend_markdown(md, day, selected)

    items_path.parent.mkdir(parents=True, exist_ok=True)
    items_path.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_bytes(new_md.encode("utf-8"))
