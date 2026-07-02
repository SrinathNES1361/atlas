from __future__ import annotations

from pathlib import Path

from atlas.adapters.pymupdf import RawDocument
from atlas.models.document import Document
from atlas.pdf.mapper import PDFMapper


class PDFExtractor:
    """
    Atlas PDF extraction pipeline.

    PDF
        ↓
    RawDocument
        ↓
    PDFMapper
        ↓
    Atlas Document
    """

    def __init__(self) -> None:
        self.mapper = PDFMapper()

    def extract(self, pdf_path: str | Path) -> Document:
        with RawDocument(pdf_path) as raw_doc:
            return self.mapper.document_from_raw(raw_doc)
