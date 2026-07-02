from __future__ import annotations

from pydantic import Field

from atlas.core.object import AtlasObject
from atlas.models.node import Node


class Page(AtlasObject):
    number: int

    width: float

    height: float

    rotation: int

    nodes: list[Node] = Field(default_factory=list)
