import os
from pathlib import Path
from .skua.pipelines import markdown_pipeline
from .skua.pipelines import Config

import click


@click.command()
@click.option('--source', default='./src', help="The directory with all the source files.")
@click.option('--destination', default='./build', help="The directory where all the HTML files will end up.")
@click.option('--templates', default='./src/templates', help="The directory containing all the templates.")
@click.option('--template-extension', default='html')
@click.option('--source-file-extension', default='md')
def render(source, destination, templates, template_extension, source_file_extension):
    pipeline = markdown_pipeline(Path(source), Path(templates), Config)