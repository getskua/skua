import pathlib
from typing import Callable, List

from skua.files import FindFilesByExtension, calculate_save_location
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

    def compile_and_save_files(self, source_directory: pathlib.Path, output_directory: pathlib.Path):
        for input_file in self.files:
            output = self.compile_file(input_file)

            output_path = calculate_save_location(input_file, source_directory, output_directory)
            if not output_path.parent.exists():
                output_path.parent.mkdir(parents=True)

            output_file = output_path.open(mode='w+')
            output_file.write(output)
            output_file.close()


def markdown_pipeline(source_dir: pathlib.Path, template_dir: pathlib.Path, config: Config):
    return HTMLPipeline(FindFilesByExtension(source_dir), MarkdownPreprocessor(config),
                        Templates(template_dir))
