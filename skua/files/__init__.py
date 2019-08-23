import glob
import os
import pathlib
from typing import List

import frontmatter

from .git import Git


def generate_output_filenames(input_files: List[str], source_dir: str, output_dir: str):
    for file in input_files:
        path = pathlib.Path(file)
        index = path.parts.index(source_dir) + 1
        pre_index = index - 1
        if pre_index >= 0:
            yield str(
                pathlib.Path('').joinpath(*path.parts[:pre_index]).joinpath(output_dir).joinpath(*path.parts[index:]))
        else:
            yield str(pathlib.Path(output_dir).joinpath(*path.parts[index:]))


def generate_sparse_index(markdown_directory, file_extension="md"):
    """
    Produces an index of all the markdown files.
    :param markdown_directory:
    :param file_extension:
    :return:
    """
    return glob.glob(os.path.join(markdown_directory, '*.' + file_extension))


def generate_detailed_index(markdown_directory, file_extension="md"):
    files: list = []
    index = generate_sparse_index(markdown_directory, file_extension)
    for file in index:
        data = dict(frontmatter.load(file))
        files.append(data)
    return files
