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

    ascender: float = 0.0

    descender: float = 0.0

    origin_x: float = 0.0

    origin_y: float = 0.0
