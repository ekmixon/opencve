import time
from contextlib import contextmanager
from functools import update_wrapper
from pathlib import Path

import click


def info(msg, nl=True):
    click.echo(f"[*] {msg}", nl=nl)


def error(msg, nl=True):
    click.echo(f"[error] {msg}", nl=nl)


def header(msg):
    click.echo("#" * len(msg))
    click.echo(msg)
    click.echo("#" * len(msg))


@contextmanager
def timed_operation(msg, nl=False):
    start = time.time()
    info(msg, nl=nl)
    yield
    click.echo(f" (done in {round(time.time() - start, 3)}s).")


def ensure_config(f):
    @click.pass_context
    def decorator(__ctx, *args, **kwargs):
        from opencve.configuration import OPENCVE_CONFIG

        if not Path(OPENCVE_CONFIG).exists():
            error("Configuration not found (use the 'init' command)")
            __ctx.exit()
        return __ctx.invoke(f, *args, **kwargs)

    return update_wrapper(decorator, f)
