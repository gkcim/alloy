# -*- coding: utf-8 -*-


import click
import os
import sys

from . import __version__


def patch_sys_argv(ctx, default_args=None):
    if default_args is None:
        default_args = []
    group_name = ctx.parent.command.name + ' ' if ctx.parent else ''
    prog_name = "{}{}".format(group_name, ctx.command.name)
    sys.argv = [prog_name] + (ctx.args or default_args)


@click.group()
@click.version_option(version=__version__)
def alo():
    pass


@click.command()
@click.option('--bind', '-b', default='127.0.0.1:8000',
              help="The socket to bind. ['127.0.0.1:8000']")
def serve(bind):
    from .app import create_app
    create_app('development')
    from .wsgi import run_app
    run_app()


@click.command()
@click.pass_context
def test(ctx):
    dirname = os.path.abspath(os.path.dirname('.'))
    tests_path = os.path.join(dirname, 'tests')
    ini_path = os.path.join(dirname, 'tests', 'pytest.ini')
    patch_sys_argv(ctx, default_args=[tests_path])
    sys.argv.append("-c{}".format(ini_path))

    from .app import create_app
    create_app('testing')

    import pytest
    ctx.exit(pytest.main())


alo.add_command(serve)
alo.add_command(test)
