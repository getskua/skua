import pathlib
import unittest

from bs4 import BeautifulSoup

from skua.preprocessors import Config
from skua.preprocessors.markdown import MarkdownPreprocessor
from skua.render import Jinja2Templates, render_jinja2_parallel


class TestRenderWithMockSite(unittest.TestCase):
    """
    Functional tests with an example website.
    """

    def setUp(self):
        self.templates = Jinja2Templates(pathlib.Path('tests/src/templates'))
        self.config = Config({
            'site_name': "Test Site!",
            'author': "Person 1",
        })
        self.md_preprocessor = MarkdownPreprocessor(self.config)

    def loadAndRenderMarkdown(self, file):
        return self.templates.render_template(**self.md_preprocessor(file))

    def test_file_1(self):
        rendered_file = self.loadAndRenderMarkdown('tests/src/blog/skua-is-a-static-site-generator.md')
        dictionary = self.md_preprocessor('tests/src/blog/skua-is-a-static-site-generator.md')

        soup = BeautifulSoup(rendered_file, 'html.parser')
        content_exists = soup.find_all('div', _class='content')
        header_h1 = soup.find('header', {'class': 'header'}).find('h1').text
        header_h3 = soup.find('header', {'class': 'header'}).find('h3').text

        self.assertTrue(header_h1 == dictionary['title'])
        self.assertTrue(header_h3 == dictionary['subtitle'])
        self.assertTrue(content_exists is not None)

    def test_parallel_processing(self):
        file_list = pathlib.Path('tests/src').rglob('*.md')
        files = []
        for file in file_list:
            files.append(self.md_preprocessor(file))
        self.assertTrue(len(render_jinja2_parallel(files, template_dir=pathlib.Path('tests/src/templates'))) > 0)
