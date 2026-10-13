from datetime import datetime, timezone

from akd.cli import build_parser, load_scored, save_scored
from akd.models import Item, Scored

NOW = datetime(2026, 10, 12, 12, tzinfo=timezone.utc)


def test_scored_cache_roundtrip(tmp_path):
    item = Item("a", "web", "T", "https://e.com/a", "body", NOW)
    scored = [Scored(item, "research", {"significance": 0.5, "relevance": 0.4, "actionability": 0.3, "novelty": 0.2}, 0.1, 0.8, low_confidence=True)]
    path = tmp_path / "scored.json"
    save_scored(scored, path)
    back = load_scored(path)
    assert back == scored


def test_parser_has_run_and_tune_commands():
    p = build_parser()
    assert p.parse_args(["run", "--dry-run"]).dry_run is True
    args = p.parse_args(["tune", "--from-cache", "--top", "5"])
    assert args.from_cache is True and args.top == 5
