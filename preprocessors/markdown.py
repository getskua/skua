import frontmatter
import markdown

from . import Preprocessor


class MarkdownPreprocessor(Preprocessor):
    def __init__(self):
        super(MarkdownPreprocessor, self).__init__()

    def preprocess(self, input_file):
        file = frontmatter.load(input_file)
        file.content = markdown.markdown(file.content)
        return file
