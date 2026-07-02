import pytest

from atlas.pdf import PDFExtractor


def test_extractor_exists():

    extractor = PDFExtractor()

    assert extractor is not None


def test_missing_pdf():
    extractor = PDFExtractor()

    with pytest.raises(FileNotFoundError):
        extractor.extract("missing.pdf")
