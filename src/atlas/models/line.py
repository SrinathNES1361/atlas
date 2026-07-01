from __future__ import annotations

from pydantic import Field

from atlas.core.geometry import Rect
from atlas.core.object import AtlasObject
from atlas.models.span import Span


class Line(AtlasObject):
    rect: Rect

    spans: list[Span] = Field(default_factory=list)

    @property
    def text(self) -> str:
        return "".join(span.text for span in self.spans)