from __future__ import annotations

from typing import Any

from atlas.adapters.pymupdf import RawDocument, RawPage
from atlas.core.enums import NodeType
from atlas.core.geometry import Rect
from atlas.models.document import Document
from atlas.models.line import Line
from atlas.models.node import Node
from atlas.models.page import Page
from atlas.models.span import Span


class PDFMapper:
    """
    Converts RawDocument objects into Atlas DOM objects.

    This module must remain independent from PyMuPDF.
    """

    @staticmethod
    def rect_from_bbox(bbox: list[float] | tuple[float, ...]) -> Rect:
        return Rect(
            x0=float(bbox[0]),
            y0=float(bbox[1]),
            x1=float(bbox[2]),
            y1=float(bbox[3]),
        )

    @classmethod
    def span_from_raw(cls, raw_span: dict[str, Any]) -> Span:
        return Span(
            text=raw_span.get("text", ""),
            rect=cls.rect_from_bbox(raw_span["bbox"]),
            font=raw_span.get("font", ""),
            font_size=float(raw_span.get("size", 0.0)),
            font_flags=int(raw_span.get("flags", 0)),
            color=int(raw_span.get("color", 0)),
            ascender=float(raw_span.get("ascender", 0.0)),
            descender=float(raw_span.get("descender", 0.0)),
            origin_x=float(raw_span.get("origin", (0, 0))[0]),
            origin_y=float(raw_span.get("origin", (0, 0))[1]),
        )

    @classmethod
    def line_from_raw(cls, raw_line: dict[str, Any]) -> Line:
        spans = [cls.span_from_raw(span) for span in raw_line.get("spans", [])]

        return Line(
            rect=cls.rect_from_bbox(raw_line["bbox"]),
            spans=spans,
        )

    @classmethod
    def node_from_raw(
        cls,
        raw_block: dict[str, Any],
        page_number: int,
    ) -> Node:

        lines = [cls.line_from_raw(line) for line in raw_block.get("lines", [])]

        return Node(
            rect=cls.rect_from_bbox(raw_block["bbox"]),
            node_type=NodeType.TEXT,
            page_number=page_number,
            rotation=0,
            lines=lines,
        )

    @classmethod
    def page_from_raw(cls, raw_page: RawPage) -> Page:

        nodes: list[Node] = []

        for block in raw_page.data.get("blocks", []):
            # Text block
            if block.get("type") == 0:
                nodes.append(
                    cls.node_from_raw(
                        block,
                        raw_page.number,
                    )
                )

        return Page(
            number=raw_page.number,
            width=raw_page.width,
            height=raw_page.height,
            rotation=raw_page.rotation,
            nodes=nodes,
        )

    @classmethod
    def document_from_raw(
        cls,
        raw_document: RawDocument,
    ) -> Document:

        pages = [cls.page_from_raw(page) for page in raw_document.pages()]

        return Document(
            path=raw_document.path,
            pages=pages,
        )
