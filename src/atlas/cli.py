from __future__ import annotations

from pathlib import Path

import typer

from atlas.pdf import PDFExtractor

app = typer.Typer(help="Atlas Scientific PDF Intelligence Engine")


@app.command()
def version() -> None:
    typer.echo("Atlas v0.1.0")


@app.command()
def extract(pdf: Path) -> None:

    extractor = PDFExtractor()

    document = extractor.extract(pdf)

    typer.echo(f"Pages : {document.page_count}")
    typer.echo(f"Nodes : {document.node_count}")
    typer.echo(f"Lines : {document.line_count}")
    typer.echo(f"Spans : {document.span_count}")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
