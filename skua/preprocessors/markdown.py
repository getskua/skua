import frontmatter
import markdown

from . import Preprocessor, Config


class MarkdownPreprocessor(Preprocessor):
    def __init__(self, config: Config):
        super(MarkdownPreprocessor, self).__init__(config)

    def preprocess(self, input_file):
        file = frontmatter.load(input_file)
        content = markdown.markdown(file.content)
        file = dict(file)
        file['content'] = content
        return file
