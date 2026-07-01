from __future__ import annotations

from pydantic import Field

from atlas.core.enums import NodeType
from atlas.core.geometry import Rect
from atlas.core.object import AtlasObject
from atlas.models.line import Line


class Node(AtlasObject):
    rect: Rect

    node_type: NodeType = NodeType.TEXT

    page_number: int

    rotation: float = 0.0

    lines: list[Line] = Field(default_factory=list)

    @property
    def text(self) -> str:
        return "\n".join(line.text for line in self.lines)