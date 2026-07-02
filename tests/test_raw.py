import pytest

from atlas.adapters.pymupdf import RawDocument


def test_invalid_pdf():

    with pytest.raises(FileNotFoundError):
        RawDocument("missing.pdf")
