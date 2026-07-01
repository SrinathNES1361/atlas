from __future__ import annotations

from atlas.core.geometry import Rect
from atlas.core.object import AtlasObject


class Span(AtlasObject):

    text: str
    rect: Rect
    font: str
    font_size: float
    font_flags: int
    color: int