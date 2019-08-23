import pathlib
from typing import List


def generate_output_filenames(input_files: List[str], source_dir: str, output_dir: str):
    for file in input_files:
        path = pathlib.Path(file)
        index = path.parts.index(source_dir) + 1
        yield str(pathlib.Path(output_dir).joinpath(*path.parts[index:]))
