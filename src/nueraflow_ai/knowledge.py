"""Explicitly registered learning sources; fetching/rights checks are future adapters."""

from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass(frozen=True)
class KnowledgeSource:
    title: str
    url: str
    kind: str
    notes: str = ""

    def validate(self) -> None:
        parsed = urlparse(self.url)
        if parsed.scheme not in {"https", "http"} or not parsed.netloc:
            raise ValueError("Source URL must be an absolute HTTP(S) URL")
        if not self.title.strip() or not self.kind.strip():
            raise ValueError("Source title and kind are required")
