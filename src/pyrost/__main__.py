"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """ROST Python Bindings."""


if __name__ == "__main__":
    main(prog_name="pyrost")  # pragma: no cover
