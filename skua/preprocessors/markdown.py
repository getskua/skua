import frontmatter
import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

from . import Preprocessor, Config


class MarkdownPreprocessor(Preprocessor):
    def __init__(self, config: Config = Config({}), site_url: str = "", extension="html"):
        super(MarkdownPreprocessor, self).__init__(config)
        self.site_url = site_url
        self.extension = extension

    def preprocess(self, input_file):
        file = frontmatter.load(input_file)
        content = markdown.markdown(file.content,
                                    extensions=[
                                        WikiLinkExtension(base_url=self.site_url, end_url="." + self.extension)])
        file = dict(file)
        file['content'] = content
        return file
