"""Command line: `python -m akd.cli run [--dry-run]` and `python -m akd.cli tune`."""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import shutil
import sys
from datetime import date, datetime, timezone
from pathlib import Path

import httpx

from akd.collectors.github import GitHubCollector
from akd.collectors.reddit import RedditCollector
from akd.collectors.web import WebCollector
from akd.config import load_config, load_profile
from akd.models import Item, Scored
from akd.pipeline import format_tune, gather, published_ids_from, rank_all, run
from akd.publish import ITEMS_RELPATH, MD_NAME
from akd.score import score_items_async
from akd.summarize import summarize

ROOT = Path(__file__).resolve().parent.parent


def save_scored(scored: list[Scored], path: Path) -> None:
    rows = [
        {
            "item": {**s.item.__dict__, "published_at": s.item.published_at.isoformat()},
            "category": s.category,
            "scores": s.scores,
            "hype_p": s.hype_p,
            "confidence": s.confidence,
            "low_confidence": s.low_confidence,
        }
        for s in scored
    ]
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")


def load_scored(path: Path) -> list[Scored]:
    out = []
    for r in json.loads(Path(path).read_text(encoding="utf-8")):
        item = Item(**{**r["item"], "published_at": datetime.fromisoformat(r["item"]["published_at"])})
        out.append(Scored(item, r["category"], r["scores"], r["hype_p"], r["confidence"], low_confidence=r["low_confidence"]))
    return out


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="akd")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="collect, rank and publish today's items")
    r.add_argument("--dry-run", action="store_true", help="write to --out instead of the real repos")
    r.add_argument("--out", type=Path, default=ROOT / "out")
    r.add_argument("--site-dir", type=Path, default=ROOT / "site", help="checkout of the site repo")
    r.add_argument("--digest-dir", type=Path, default=ROOT)
    r.add_argument("--day", type=date.fromisoformat, default=None)
    t = sub.add_parser("tune", help="score a sample and print the top/bottom for weight tuning")
    t.add_argument("--top", type=int, default=20)
    t.add_argument("--cache", type=Path, default=ROOT / "out" / "scored.json")
    t.add_argument("--from-cache", action="store_true", help="re-rank cached scores without calling Jev")
    return p


def _score_sync(items: list[Item], profile: str, low_conf: float) -> list[Scored]:
    from typesafe_sdk import AsyncTypeSafeClient

    async def go() -> list[Scored]:
        async with AsyncTypeSafeClient() as client:
            return await score_items_async(items, profile, client, low_conf)

    return asyncio.run(go())


def _collectors(cfg, client: httpx.Client):
    return [GitHubCollector(cfg, client), RedditCollector(cfg, client), WebCollector(cfg, client)]


def _read_doc(site_dir: Path) -> dict:
    path = site_dir / ITEMS_RELPATH
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def cmd_run(args) -> int:
    import anthropic

    cfg = load_config(ROOT / "config.yaml")
    profile = load_profile(ROOT / "profile.yaml")
    day = args.day or datetime.now(timezone.utc).date()
    published = published_ids_from(_read_doc(args.site_dir), day)

    if args.dry_run:
        digest_dir, site_dir = args.out / "digest", args.out / "site"
        digest_dir.mkdir(parents=True, exist_ok=True)
        if (args.digest_dir / MD_NAME).exists():
            shutil.copyfile(args.digest_dir / MD_NAME, digest_dir / MD_NAME)
        if (args.site_dir / ITEMS_RELPATH).exists():
            (site_dir / ITEMS_RELPATH).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(args.site_dir / ITEMS_RELPATH, site_dir / ITEMS_RELPATH)
    else:
        digest_dir, site_dir = args.digest_dir, args.site_dir

    claude = anthropic.Anthropic()
    with httpx.Client() as http:
        selected = run(
            cfg,
            profile,
            _collectors(cfg, http),
            lambda items, prof: _score_sync(items, prof, cfg.low_confidence_threshold),
            lambda sel, prof: summarize(sel, claude, prof),
            published,
            day,
            digest_dir,
            site_dir,
        )
    print(f"published {len(selected)} items for {day} ({'dry-run -> ' + str(args.out) if args.dry_run else 'live'})")
    return 0


def cmd_tune(args) -> int:
    cfg = load_config(ROOT / "config.yaml")
    if args.from_cache:
        scored = load_scored(args.cache)
    else:
        profile = load_profile(ROOT / "profile.yaml")
        with httpx.Client() as http:
            items = gather(cfg, _collectors(cfg, http), set(), datetime.now(timezone.utc))
        scored = _score_sync(items, profile, cfg.low_confidence_threshold)
        save_scored(scored, args.cache)
    print(format_tune(rank_all(scored, cfg), args.top))
    return 0


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    args = build_parser().parse_args(argv)
    return cmd_run(args) if args.cmd == "run" else cmd_tune(args)


if __name__ == "__main__":
    sys.exit(main())
