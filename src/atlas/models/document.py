from __future__ import annotations

from pathlib import Path

from pydantic import Field

from atlas.core.object import AtlasObject
from atlas.models.page import Page


class Document(AtlasObject):
    path: Path

    pages: list[Page] = Field(default_factory=list)

    @property
    def page_count(self) -> int:
        return len(self.pages)

    @property
    def node_count(self) -> int:
        return sum(len(page.nodes) for page in self.pages)

    @property
    def line_count(self) -> int:
        return sum(len(node.lines) for page in self.pages for node in page.nodes)

    @property
    def span_count(self) -> int:
        return sum(
            len(line.spans) for page in self.pages for node in page.nodes for line in node.lines
        )
