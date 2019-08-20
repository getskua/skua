import unittest

from skua.preprocessors import Config
from skua.preprocessors.markdown import MarkdownPreprocessor
from skua.render import Templates


class TestRenderWithMockSite(unittest.TestCase):
    def setUp(self):
        self.templates = Templates(__name__, 'tests/src/templates')
        self.config = Config({
            'site_name': "Test Site!",
            'author': "Person 1"
        })
        self.md_preprocessor = MarkdownPreprocessor(self.config)

    def loadAndRenderMarkdown(self, file):
        print(self.md_preprocessor(file))
        return self.templates.render_template(**self.md_preprocessor(file))

    def testFile1(self):
        rendered_file = self.loadAndRenderMarkdown('tests/src/blog/skua-is-a-static-site-generator.md')
        print(rendered_file)
