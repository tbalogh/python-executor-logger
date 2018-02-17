# -*- coding: utf-8 -*-

"""Console script for executor_logger."""

import click


@click.command()
def main(args=None):
    """Console script for executor_logger."""
    click.echo("Replace this message by putting your code into "
               "executor_logger.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
