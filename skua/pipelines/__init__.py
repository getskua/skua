import pathlib
from typing import Callable, List

from skua.files import FindFilesByExtension
from skua.preprocessors import Config
from skua.preprocessors.markdown import MarkdownPreprocessor
from skua.render import Templates


class HTMLPipeline(object):
    def __init__(self, file_finder, *args):
        """
        Compiles markup into HTML.
        :param file_finder: A callable entity which returns a list of `pathlib.Path` objects.
        :param args: Callable entities to compile the files.
        """
        self.pipeline: List[Callable] = list(args)
        self.file_finder = file_finder
        self.files: List[pathlib.Path] = list(self.file_finder())

    def compile_file(self, file: pathlib.Path):
        for step in self.pipeline:
            if isinstance(step, Templates):
                file = step(**file)
            else:
                file = step(file)
        return file

    def save_files(self):

        for input_file, output_file in zip(self.files):
            output = self.compile_file(input_file)
            with open(output_file, 'w+') as f:
                f.write(output)

    def render_file(self, file: pathlib.Path):
        pass


def markdown_pipeline(source_dir: pathlib.Path, template_dir: pathlib.Path, config: Config):
    return HTMLPipeline(FindFilesByExtension(source_dir), MarkdownPreprocessor(config),
                        Templates(template_dir))
