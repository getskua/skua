import pathlib
import unittest

from bs4 import BeautifulSoup

from skua.pipelines import markdown_pipeline
from skua.preprocessors import Config
from skua.preprocessors.markdown import MarkdownPreprocessor
from skua.render import Templates


class TestMarkdownPipelineFunction(unittest.TestCase):
    def setUp(self):
        self.pipeline = markdown_pipeline(pathlib.Path('tests/src'), pathlib.Path('tests/src/templates'),
                                          Config({'site_name': 'Hello World!', 'site_author': 'Me!'}))

    def test_creation(self):
        expectation = [MarkdownPreprocessor, Templates]
        for step, instance in zip(self.pipeline.pipeline, expectation):
            self.assertTrue(isinstance(step, instance))

    def test_rendering(self):
        output = self.pipeline.compile_file('tests/src/blog/skua-is-a-static-site-generator.md')

        dictionary = self.pipeline.pipeline[0]('tests/src/blog/skua-is-a-static-site-generator.md')

        soup = BeautifulSoup(output, 'html.parser')
        content_exists = soup.find_all('div', _class='content')
        header_h1 = soup.find('header', {'class': 'header'}).find('h1').text
        header_h3 = soup.find('header', {'class': 'header'}).find('h3').text

        self.assertTrue(header_h1 == dictionary['title'])
        self.assertTrue(header_h3 == dictionary['subtitle'])
        self.assertTrue(content_exists is not None)

    def test_file_saving(self):
        self.pipeline.compile_and_save_files(pathlib.Path('tests/src'), pathlib.Path('tests/build'))


class TestConfig(unittest.TestCase):
    def test_loading_from_file(self):
        config = Config.from_file(pathlib.Path('tests/src/config.json'))
        expectation = {
            "site_name": "Hello World!",
            "site_author": "Me!"
        }
        self.assertTrue(len(expectation) == len(config))
        for key in expectation.keys():
            self.assertTrue(key in config.config)
            self.assertTrue(config.config[key] == expectation[key])
