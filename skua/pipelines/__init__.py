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

    def compile_file(self, file):
        """
        Turn a single file into an HTML document
        :param file:
        :return:
        """
        for step in self.pipeline:
            if isinstance(step, Templates):
                file = step(**file)
            else:
                file = step(file)
        return file

    def __call__(self, *args, **kwargs):
        files = self.file_finder()
        for input_file, output_file in zip(files[0], files[1]):
            output = self.compile_file(input_file)
            with open(output_file, 'w+') as f:
                f.write(output)


def markdown_pipeline(source_dir, template_dir: str, config: Config):
    return HTMLPipeline(FindFilesByExtension(source_dir), MarkdownPreprocessor(config),
                        Templates(template_dir))
