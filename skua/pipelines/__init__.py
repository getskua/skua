from typing import Callable, List

from skua.preprocessors import Config
from skua.preprocessors.markdown import MarkdownPreprocessor
from skua.render import Templates


class Pipeline(object):
    def __init__(self, file_finder, *args):
        self.pipeline: List[Callable] = list(args)
        self.file_finder = file_finder

    def compile_file(self, file):
        for step in self.pipeline:
            if isinstance(step, Templates):
                file = step(**file)
            else:
                file = step(file)
        return file

    def __call__(self, *args, **kwargs):
        files = self.file_finder()
        for input_file, output_file in files:
            output = self.compile_file(input_file)
            with open(output_file, 'w+') as f:
                f.write(output)


def markdown_pipeline(import_name, template_dir: str, config: Config):
    return Pipeline(MarkdownPreprocessor(config), Templates(import_name, template_dir))
