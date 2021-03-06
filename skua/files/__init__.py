import pathlib
import shutil
from typing import Iterable, List, Union

import frontmatter


class FindFilesByExtension(object):
    def __init__(self, source_directory: Union[pathlib.Path, str] = pathlib.Path("src"), extension="md"):
        if isinstance(source_directory, str):
            source_directory = pathlib.Path(source_directory)
        self.source_directory: pathlib.Path = source_directory
        self.extension: str = extension

    def __call__(self, *args, **kwargs):
        return self.source_directory.glob('**/*.' + self.extension)


def calculate_save_location(file: Union[pathlib.Path, str], source_directory: Union[pathlib.Path, str],
                            output_directory: Union[pathlib.Path, str], output_format: str = 'html') -> pathlib.Path:
    """
    Calculates where a file should be saved.
    :param file: A pathlib.Path object pointing to the file.
    :param source_directory: Where all the source files are stored.
    :param output_directory: Where all the HTML fies should be placed.
    :param output_format: The extension for the save location.
    :return:
    """
    if isinstance(file, str):
        file = pathlib.Path(file)
    if isinstance(source_directory, str):
        source_directory = pathlib.Path(source_directory)
    if isinstance(output_directory, str):
        output_directory = pathlib.Path(output_directory)

    directory: pathlib.Path = file.parent
    start, stop = directory.parts.index(source_directory.parts[0]), directory.parts.index(source_directory.parts[-1])
    pre: pathlib.Path = pathlib.Path(''.join(directory.parts[:start]))
    post: pathlib.Path = pathlib.Path(''.join(directory.parts[stop + 1:]))
    return pathlib.Path(pre).joinpath(output_directory).joinpath(post).joinpath(
        file.stem + '.' + output_format)


def generate_index(source_directory: Union[pathlib.Path, str] = pathlib.Path("src/blog"), extension: str = "md",
                   recursive: bool = False):
    """
    Returns a generator object containing dictionaries containing the frontmatter, contents as well as a pathlib.Path
    object containing the absolute path to each file.
    :param recursive: Whether or not to search in subdirectories as well as the current directory.
    :param source_directory: The folder for which you want to generate the index.
    :param extension: The extension for files (by default `.md`)
    :return:
    """
    if isinstance(source_directory, str):
        source_directory = pathlib.Path(source_directory)
    files = source_directory.glob('**/*.' + extension) if recursive else source_directory.glob('*.' + extension)
    for file in files:
        yield {**frontmatter.load(str(file)), **{'file_path': file},
               **{'content': frontmatter.load(str(file)).content}}


def copy_files(source_directory: Union[pathlib.Path, str] = pathlib.Path('src'),
               output_directory: Union[pathlib.Path, str] = pathlib.Path('build'),
               extensions: Iterable[str] = ("html",),
               recursive: bool = False):
    """
    Copy files from the source directory to the destination directory.

    :param source_directory:
    :param output_directory:
    :param extensions:
    :param recursive:
    :return:
    """
    if isinstance(source_directory, str):
        source_directory = pathlib.Path(source_directory)
    if isinstance(output_directory, str):
        output_directory = pathlib.Path(output_directory)

    glob_patterns: List[str] = ['**/*.' + extension if recursive else '*.' + extension for extension in extensions]
    files = []
    for pattern in glob_patterns:
        files: List[pathlib.Path] = [*files, *source_directory.glob(pattern)]
    for file in files:
        if not file.exists():
            raise FileNotFoundError("The file {} cannot be found.".format(str(file)))

        output_location = calculate_save_location(file, source_directory, output_directory,
                                                  output_format=file.suffix[1:])

        directory: pathlib.Path = output_location.parent
        if not directory.exists():
            directory.mkdir(parents=True)

        source_file = str(file)

        output_location = str(output_location)

        shutil.copy(source_file, output_location)
