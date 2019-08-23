import pathlib
from typing import List

from .git import Git


def generate_output_filenames(input_files: List[str], source_dir: str, output_dir: str):
    for file in input_files:
        path = pathlib.Path(file)
        index = path.parts.index(source_dir) + 1
        pre_index = index - 2
        if pre_index >= 0:
            yield str(
                pathlib.Path('').joinpath(*path.parts[:pre_index]).joinpath(output_dir).joinpath(*path.parts[index:]))
        else:
            yield str(pathlib.Path(output_dir).joinpath(*path.parts[index:]))
