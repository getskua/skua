import glob
import os
import pathlib
from typing import List, Dict

import frontmatter

from .git import Git


class Files(object):
    def __init__(self, *args, **kwargs):
        pass

    def find_all(self, *args, **kwargs) -> List[Dict]:
        pass

    def __call__(self, *args, **kwargs) -> List[Dict]:
        return self.find_all()


class AllMarkdownFiles(Files):
    def __init__(self, input_dir, output_dir, detailed_indexing=True):
        super(AllMarkdownFiles, self).__init__()
        """
        Finds all markdown files in a directory and lists them. 
        """
        self.index: bool = detailed_indexing
        self.input_dir = input_dir
        self.output_dir = output_dir

    def find_all(self):
        """
        Find all the files. This method is accessible through the __call__ method of the class.
        :return: A generator containing input filename, output filename tuple pairs.
        """
        files = generate_detailed_index(self.input_dir, file_extension="md")
        return zip(files, generate_output_filenames(files, source_dir=self.input_dir, output_dir=self.output_dir))


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
