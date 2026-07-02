from pathlib import Path

from atlas.pdf.extractor import PDFExtractor


def test_extract_real_pdf() -> None:
    pdf = Path("examples/yjoh-23-187.pdf")

    assert pdf.exists()

    extractor = PDFExtractor()

    document = extractor.extract(pdf)

    assert document.page_count > 0
    assert document.node_count > 0
    assert document.line_count > 0
    assert document.span_count > 0