from typing import Callable, List, Dict

from skua.preprocessors import Config
from skua.preprocessors.markdown import MarkdownPreprocessor
from skua.render import Templates


class Pipeline(object):
    def __init__(self, *args):
        self.pipeline: List[Callable] = list(args)

    def __call__(self, file):
        for step in self.pipeline:
            if isinstance(step, Templates):
                file = step(**file)
            else:
                file = step(file)
        return file

    def apply_to_files(self, files):
        """
        Apply this to a list of files.
        :param files: A list of files
        :return: A generator object containing all the preprocessed files.
        """
        for file in files:
            yield self.__call__(file)

    def apply_to_files_and_save(self, files: List[Dict], output_folders):
        for i, file in enumerate(files):
            output = self.__call__(file)
            with open(output_folders[i], 'w+') as f:
                f.write(output)


def markdown_pipeline(import_name, template_dir: str, config: Config):
    return Pipeline(Templates(import_name, template_dir), MarkdownPreprocessor(config))