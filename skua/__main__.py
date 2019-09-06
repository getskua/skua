import click


@click.command()
@click.option('--input_directory', default='./src', help="The source directory for all your files")
@click.option('--output_directory', default='./build', help="Where all the HTML files should be saved")
@click.option('--template-folder', default='./src/templates', help="The location of all the HTML templates.")
@click.option('--config-location', default='config.json', help="Where the JSON Config object is stored.")
@click.option('--markdown-extension', default='md', help="The extension ofr markdown files.")
def compile_files(input_directory: str, output_directory: str, template_folder: str, config_location: str,
                  markdown_extension: str):
    pass
