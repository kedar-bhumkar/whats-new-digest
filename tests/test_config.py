from pathlib import Path

import pytest

from akd.config import load_config, load_profile

CONFIG_YAML = """
weights:
  significance: 0.45
  relevance: 0.25
  actionability: 0.20
  novelty: 0.10
max_picks: 5
max_notable: 10
min_notable_rank: 0.35
hype_penalty: 0.5
low_confidence_threshold: 0.4
window_days: 60
subreddits: [LocalLLaMA]
feeds: ["https://example.com/feed.xml"]
github_topics: [llm]
github_watchlist: [anthropics/claude-code]
"""


def write(tmp_path: Path, text: str) -> Path:
    p = tmp_path / "config.yaml"
    p.write_text(text, encoding="utf-8")
    return p


def test_load_config_defaults(tmp_path):
    cfg = load_config(write(tmp_path, CONFIG_YAML))
    assert cfg.weights == {
        "significance": 0.45,
        "relevance": 0.25,
        "actionability": 0.20,
        "novelty": 0.10,
    }
    assert cfg.max_picks == 5
    assert cfg.max_notable == 10
    assert cfg.hype_penalty == 0.5
    assert cfg.window_days == 60
    assert cfg.subreddits == ["LocalLLaMA"]


def test_weights_must_sum_to_one(tmp_path):
    bad = CONFIG_YAML.replace("significance: 0.45", "significance: 0.35")
    with pytest.raises(ValueError):
        load_config(write(tmp_path, bad))


def test_load_profile_returns_text(tmp_path):
    p = tmp_path / "profile.yaml"
    p.write_text("stack:\n  - Claude Code\n", encoding="utf-8")
    assert "Claude Code" in load_profile(p)


def test_repo_config_and_profile_load():
    root = Path(__file__).resolve().parent.parent
    cfg = load_config(root / "config.yaml")
    assert cfg.max_picks == 5
    assert load_profile(root / "profile.yaml").strip()
