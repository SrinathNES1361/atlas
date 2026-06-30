import typer

app = typer.Typer(help="Atlas - Scientific Document Intelligence Engine")


@app.command()
def version():
    """Show Atlas version."""
    typer.echo("Atlas v0.1.0")


@app.command()
def extract(pdf: str):
    """Extract a PDF (placeholder)."""
    typer.echo(f"Extracting {pdf}")


def main():
    app()


if __name__ == "__main__":
    main()
