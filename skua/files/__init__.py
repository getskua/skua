import pathlib
from typing import Generator

import frontmatter


class FindFilesByExtension(object):
    def __init__(self, source_directory: pathlib.Path = pathlib.Path("src"), extension="md"):
        self.source_directory: pathlib.Path = source_directory
        self.extension: str = extension

    def __call__(self, *args, **kwargs):
        return self.source_directory.glob('**/*.' + self.extension)


def calculate_save_location(file: pathlib.Path, source_directory: pathlib.Path,
                            output_directory: pathlib.Path, output_format: str = 'html') -> pathlib.Path:
    """
    Calculates where a file should be saved.
    :param file: A pathlib.Path object pointing to the file.
    :param source_directory: Where all the source files are stored.
    :param output_directory: Where all the HTML fies should be placed.
    :param output_format: The extension for the save location.
    :return:
    """
    directory: pathlib.Path = file.parent
    start, stop = directory.parts.index(source_directory.parts[0]), directory.parts.index(source_directory.parts[-1])
    pre: pathlib.Path = pathlib.Path(''.join(directory.parts[:start]))
    post: pathlib.Path = pathlib.Path(''.join(directory.parts[stop + 1:]))
    return pathlib.Path(pre).joinpath(output_directory).joinpath(post).joinpath(
        file.stem + '.' + output_format)


def generate_index(source_directory: pathlib.Path = pathlib.Path("src/blog"), extension="md", recursive=False):
    """
    Returns a generator object containing dictionaries containing the frontmatter, contents as well as a pathlib.Path
    object containing the absolute path to each file.
    :param recursive: Whether or not to search in subdirectories as well as the current directory.
    :param source_directory: The folder for which you want to generate the index.
    :param extension: The extension for files (by default `.md`)
    :return:
    """
    files = source_directory.glob('**/*.' + extension) if recursive else source_directory.glob('*.' + extension)
    for file in files:
        yield {**frontmatter.load(str(file)), **{'file_path': file}}
