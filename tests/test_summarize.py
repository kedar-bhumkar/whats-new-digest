from datetime import datetime, timezone
from types import SimpleNamespace

from akd.models import Item, Scored, Selected
from akd.summarize import MAX_WHY, summarize

NOW = datetime(2026, 10, 12, tzinfo=timezone.utc)


def selected(n: int) -> Selected:
    item = Item(f"id{n}", "web", f"Title {n}", f"https://e.com/{n}", f"body {n}", NOW)
    scored = Scored(item, "dev_tooling", {"significance": 0.5, "relevance": 0.5, "actionability": 0.5, "novelty": 0.5}, 0.0, 0.9)
    return Selected(scored, "pick")


class FakeClaude:
    def __init__(self, text="Cheap fast tier for subagents.", fail_on=None):
        self.text = text
        self.fail_on = fail_on
        self.prompts = []
        self.messages = SimpleNamespace(create=self._create)

    def _create(self, **kwargs):
        prompt = kwargs["messages"][0]["content"]
        self.prompts.append(prompt)
        if self.fail_on and self.fail_on in prompt:
            raise RuntimeError("api down")
        return SimpleNamespace(content=[SimpleNamespace(type="text", text=self.text)])


def test_fills_why_for_every_selected():
    out = summarize([selected(1), selected(2)], FakeClaude())
    assert [s.why for s in out] == ["Cheap fast tier for subagents."] * 2


def test_why_truncated_to_200_chars_and_single_line():
    out = summarize([selected(1)], FakeClaude(text="word " * 100 + "\nsecond line"))
    assert len(out[0].why) <= MAX_WHY == 200
    assert "\n" not in out[0].why


def test_failure_leaves_why_empty_and_continues():
    out = summarize([selected(1), selected(2)], FakeClaude(fail_on="Title 1"))
    assert out[0].why == ""
    assert out[1].why != ""


def test_prompt_marks_item_as_untrusted_data_and_includes_profile():
    client = FakeClaude()
    summarize([selected(1)], client, profile="MY STACK")
    prompt = client.prompts[0]
    assert "MY STACK" in prompt
    assert "<item>" in prompt and "Title 1" in prompt
    assert "do not follow" in prompt.lower()
