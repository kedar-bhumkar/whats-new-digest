"""URL-based dedupe.

NOTE (flagged simplification): near-duplicate detection by title is NOT implemented.
Two outlets covering the same story under different URLs are kept as two items.
If title-level dedupe is added, it must use embeddings, not term overlap.
"""

from __future__ import annotations

import hashlib
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from akd.models import Item

_TRACKING_PREFIXES = ("utm_",)
_TRACKING_KEYS = {"ref", "fbclid", "gclid", "mc_cid", "mc_eid"}


def canonical_url(url: str) -> str:
    parts = urlsplit(url.strip())
    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    query = [
        (k, v)
        for k, v in parse_qsl(parts.query, keep_blank_values=True)
        if k.lower() not in _TRACKING_KEYS and not k.lower().startswith(_TRACKING_PREFIXES)
    ]
    path = parts.path.rstrip("/")
    scheme = "https" if parts.scheme.lower() in ("http", "https") else parts.scheme.lower()
    return urlunsplit((scheme, host, path, urlencode(sorted(query)), ""))


def item_id(url: str) -> str:
    return hashlib.sha256(canonical_url(url).encode("utf-8")).hexdigest()[:16]


def dedupe(items: list[Item], published_ids: set[str]) -> list[Item]:
    seen: set[str] = set()
    out: list[Item] = []
    for item in items:
        key = item_id(item.url)
        if key in seen or key in published_ids or item.id in published_ids:
            continue
        seen.add(key)
        out.append(item)
    return out
