from atlas.pdf.mapper import PDFMapper


def test_rect():

    rect = PDFMapper.rect_from_bbox([0, 0, 100, 200])

    assert rect.width == 100
    assert rect.height == 200


def test_span():

    raw = {
        "text": "Atlas",
        "bbox": [0, 0, 100, 20],
        "font": "Arial",
        "size": 12,
        "flags": 0,
        "color": 0,
    }

    span = PDFMapper.span_from_raw(raw)

    assert span.text == "Atlas"
    assert span.font == "Arial"
    assert span.font_size == 12
