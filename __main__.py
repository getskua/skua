import os
from pathlib import Path

import click


@click.command()
@click.option('--source', default='./src', help="The directory with all the source files.")
@click.option('--destination', default='./_dist', help="The directory where all the HTML files will end up.")
def render_files(source, destination):
    filetree = Path().glob(os.path.join(os.path.abspath(source), '**', '*.*'))


if __name__ == '__main__':
    render_files()
