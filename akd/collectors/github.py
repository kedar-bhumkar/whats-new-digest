from __future__ import annotations

import logging
import os
from datetime import datetime, timedelta, timezone

import httpx

from akd.collectors.base import clip, get
from akd.config import Config
from akd.dedupe import item_id
from akd.models import Item

log = logging.getLogger("akd.collectors.github")
API = "https://api.github.com"
LOOKBACK_DAYS = 3
MIN_STARS = 50


def _dt(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


class GitHubCollector:
    """New repos per configured topic (created recently, above a star floor) plus
    releases of a watchlist of repos."""

    name = "github"

    def __init__(self, cfg: Config, client: httpx.Client, now: datetime | None = None) -> None:
        self.cfg = cfg
        self.client = client
        self.now = now or datetime.now(timezone.utc)

    def _headers(self) -> dict[str, str]:
        headers = {"Accept": "application/vnd.github+json"}
        token = os.environ.get("GITHUB_TOKEN")
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers

    def collect(self) -> list[Item]:
        since = (self.now - timedelta(days=LOOKBACK_DAYS)).strftime("%Y-%m-%d")
        items: list[Item] = []
        for topic in self.cfg.github_topics:
            url = (
                f"{API}/search/repositories?q=topic:{topic}+created:>{since}"
                f"+stars:>{MIN_STARS}&sort=stars&order=desc&per_page=10"
            )
            try:
                data = get(self.client, url, headers=self._headers()).json()
            except Exception:
                log.exception("github search failed for topic %s", topic)
                continue
            for repo in data.get("items", []):
                items.append(
                    Item(
                        id=item_id(repo["html_url"]),
                        source="github",
                        title=repo["full_name"],
                        url=repo["html_url"],
                        text=clip(f"{repo.get('description') or ''} (stars: {repo.get('stargazers_count', 0)})"),
                        published_at=_dt(repo["created_at"]),
                    )
                )
        cutoff = self.now - timedelta(days=LOOKBACK_DAYS)
        for repo_name in self.cfg.github_watchlist:
            try:
                releases = get(
                    self.client, f"{API}/repos/{repo_name}/releases?per_page=3", headers=self._headers()
                ).json()
            except Exception:
                log.exception("github releases failed for %s", repo_name)
                continue
            for rel in releases:
                if rel.get("draft") or _dt(rel["published_at"]) < cutoff:
                    continue
                items.append(
                    Item(
                        id=item_id(rel["html_url"]),
                        source="github",
                        title=f"{repo_name} {rel.get('name') or rel['tag_name']}",
                        url=rel["html_url"],
                        text=clip(rel.get("body") or ""),
                        published_at=_dt(rel["published_at"]),
                    )
                )
        return items
