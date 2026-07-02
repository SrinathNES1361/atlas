from pathlib import Path

from atlas.core.enums import NodeType
from atlas.core.geometry import Rect
from atlas.models import Document, Line, Node, Page, Span


def test_span():
    span = Span(
        text="Atlas",
        rect=Rect(x0=0, y0=0, x1=100, y1=20),
        font="Arial",
        font_size=12,
        font_flags=0,
        color=0,
    )

    assert span.text == "Atlas"


def test_line():
    span = Span(
        text="Hello",
        rect=Rect(x0=0, y0=0, x1=50, y1=20),
        font="Arial",
        font_size=12,
        font_flags=0,
        color=0,
    )

    line = Line(
        rect=Rect(x0=0, y0=0, x1=100, y1=20),
        spans=[span],
    )

    assert line.text == "Hello"


def test_node():
    span = Span(
        text="Atlas",
        rect=Rect(x0=0, y0=0, x1=50, y1=20),
        font="Arial",
        font_size=12,
        font_flags=0,
        color=0,
    )

    line = Line(
        rect=Rect(x0=0, y0=0, x1=50, y1=20),
        spans=[span],
    )

    node = Node(
        rect=Rect(x0=0, y0=0, x1=100, y1=100),
        page_number=1,
        node_type=NodeType.TEXT,
        lines=[line],
    )

    assert node.text == "Atlas"


def test_document():
    page = Page(
        number=1,
        width=595,
        height=842,
        rotation=0,
    )

    document = Document(
        path=Path("sample.pdf"),
        pages=[page],
    )

    assert document.page_count == 1
    assert document.node_count == 0
    assert document.line_count == 0
    assert document.span_count == 0
