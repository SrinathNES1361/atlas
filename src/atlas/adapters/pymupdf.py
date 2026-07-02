from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path
from types import TracebackType
from typing import Any

import pymupdf


class RawPage:
    """
    Immutable representation of a PyMuPDF page.

    The rest of Atlas never sees PyMuPDF objects.
    """

    __slots__ = (
        "data",
        "height",
        "number",
        "rotation",
        "width",
    )

    def __init__(
        self,
        number: int,
        width: float,
        height: float,
        rotation: int,
        data: dict[str, Any],
    ) -> None:
        self.number = number
        self.width = width
        self.height = height
        self.rotation = rotation
        self.data = data


class RawDocument:
    """
    Thin adapter around PyMuPDF.

    This is the ONLY file in Atlas that directly interacts with
    PyMuPDF. The rest of the project consumes RawPage objects.
    """

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

        if not self.path.exists():
            raise FileNotFoundError(self.path)

        # PyMuPDF currently has incomplete typing support.
        self._doc: Any = pymupdf.open(self.path)

    def __enter__(self) -> RawDocument:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.close()

    def __len__(self) -> int:
        return len(self._doc)

    @property
    def page_count(self) -> int:
        return len(self._doc)

    def pages(self) -> Iterator[RawPage]:
        """
        Iterate over every page in the PDF.

        Always returns PyMuPDF rawdict output.
        """

        page_count = len(self._doc)

        for index in range(page_count):
            page: Any = self._doc.load_page(index)

            raw: dict[str, Any] = page.get_text(
                "rawdict",
                sort=False,
            )

            yield RawPage(
                number=index + 1,
                width=float(page.rect.width),
                height=float(page.rect.height),
                rotation=int(page.rotation),
                data=raw,
            )

    def close(self) -> None:
        if self._doc is not None:
            self._doc.close()
