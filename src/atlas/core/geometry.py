from __future__ import annotations

from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True, slots=True)
class Rect:
    """
    Immutable rectangle.

    Coordinates follow the PDF coordinate system.

    x0,y0 = top-left

    x1,y1 = bottom-right
    """

    x0: float
    y0: float
    x1: float
    y1: float

    @property
    def width(self) -> float:
        return self.x1 - self.x0

    @property
    def height(self) -> float:
        return self.y1 - self.y0

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def center(self) -> tuple[float, float]:
        return (
            (self.x0 + self.x1) / 2,
            (self.y0 + self.y1) / 2,
        )

    def to_tuple(self) -> tuple[float, float, float, float]:
        return (
            self.x0,
            self.y0,
            self.x1,
            self.y1,
        )

    def contains(self, other: Rect) -> bool:
        return (
            self.x0 <= other.x0
            and self.y0 <= other.y0
            and self.x1 >= other.x1
            and self.y1 >= other.y1
        )

    # Intersection.
    def intersects(self, other: Rect) -> bool:
        return not (
            self.x1 < other.x0 or self.x0 > other.x1 or self.y1 < other.y0 or self.y0 > other.y1
        )

    # Intersection rectangle.
    def intersection(self, other: Rect) -> Rect | None:
        if not self.intersects(other):
            return None

        return Rect(
            max(self.x0, other.x0),
            max(self.y0, other.y0),
            min(self.x1, other.x1),
            min(self.y1, other.y1),
        )

    def union(self, other: Rect) -> Rect:
        return Rect(
            min(self.x0, other.x0),
            min(self.y0, other.y0),
            max(self.x1, other.x1),
            max(self.y1, other.y1),
        )

    def iou(self, other: Rect) -> float:

        inter = self.intersection(other)

        if inter is None:
            return 0.0

        return inter.area / (self.area + other.area - inter.area)

    def distance(self, other: Rect) -> float:
        cx1, cy1 = self.center
        cx2, cy2 = other.center

        return sqrt((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2)

    def translate(
        self,
        dx: float,
        dy: float,
    ) -> Rect:

        return Rect(
            x0=self.x0 + dx,
            y0=self.y0 + dy,
            x1=self.x1 + dx,
            y1=self.y1 + dy,
        )

    def expand(
        self,
        margin: float,
    ) -> Rect:

        return Rect(
            x0=self.x0 - margin,
            y0=self.y0 - margin,
            x1=self.x1 + margin,
            y1=self.y1 + margin,
        )
