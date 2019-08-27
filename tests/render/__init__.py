import unittest

from bs4 import BeautifulSoup

from skua.preprocessors import Config
from skua.preprocessors.markdown import MarkdownPreprocessor
from skua.render import Templates


class TestRenderWithMockSite(unittest.TestCase):
    """
    Functional tests with an example website.
    """

    def setUp(self):
        self.templates = Templates('tests/src/templates')
        self.config = Config({
            'site_name': "Test Site!",
            'author': "Person 1"
        })
        self.md_preprocessor = MarkdownPreprocessor(self.config)

    def loadAndRenderMarkdown(self, file):
        return self.templates.render_template(**self.md_preprocessor(file))

    def testFile1(self):
        rendered_file = self.loadAndRenderMarkdown('tests/src/blog/skua-is-a-static-site-generator.md')
        dictionary = self.md_preprocessor('tests/src/blog/skua-is-a-static-site-generator.md')

        soup = BeautifulSoup(rendered_file, 'html.parser')
        content_exists = soup.find_all('div', _class='content')
        header_h1 = soup.find('header', {'class': 'header'}).find('h1').text
        header_h3 = soup.find('header', {'class': 'header'}).find('h3').text

        self.assertTrue(header_h1 == dictionary['title'])
        self.assertTrue(header_h3 == dictionary['subtitle'])
        self.assertTrue(content_exists is not None)
