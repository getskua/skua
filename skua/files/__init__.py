import os
from typing import List


def generate_output_filenames(input_files: List[str], source_dir: str, output_dir: str):
    for file in input_files:
        # Thanks to (link below) for the suggestion as to how to split a path into its individual components
        # https://stackoverflow.com/questions/3167154/how-to-split-a-dos-path-into-its-components-in-python#answer-16595356
        path = os.path.normpath(file)
        path = os.path.split(os.sep)

        split_index: int = None
        for i, directory in path:
            if directory == source_dir:
                split_index = i
                break
        if not split_index:
            raise AttributeError("All files must be located in the source directory!")
        new_path = path[split_index:]
        yield os.path.join(output_dir, *new_path)
