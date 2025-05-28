# -*- coding: utf-8 -*-

"""Console script for {{cookiecutter.project_slug}}."""
import contextlib
import logging
import os
import sys

import click
from dotenv import load_dotenv
from {{cookiecutter.project_slug}}.logs import config_log


# if dotenv file, load it
dotenv_path = os.environ.get("{{cookiecutter.project_prefix}}_DOTENV_PATH", None)
if dotenv_path:
    # BEWARE that dotenv overrides what's already in env
    load_dotenv(dotenv_path, override=True)


# provide a file to log stuff, otherwise it's console only
# logfile = "{}/logs/cli.log".format(
#    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# )
# config_log(logfile=logfile)
config_log()
logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--arg",
    default="value",
    help="some argument for this command",
)
def cli(arg):
    click.echo("arg is {}".format(arg))
    logger.info("you can log as well, it prints useful info, and arg is {}".format(arg))


# from http://stackoverflow.com/a/29824059
@contextlib.contextmanager
def _smart_open(filename, mode="Ur"):
    if filename == "-":
        if mode is None or mode == "" or "r" in mode:
            fhandle = sys.stdin
        else:
            fhandle = sys.stdout
    else:
        fhandle = open(filename, mode)

    try:
        yield fhandle
    finally:
        if filename != "-":
            fhandle.close()


if __name__ == "__main__":
    # return exit code from cli(), instead of main
    sys.exit(cli())  # pragma: no cover
