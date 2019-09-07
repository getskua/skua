import pathlib
import unittest

from skua.preprocessors import Config
from skua.preprocessors.markdown import MarkdownPreprocessor


class TestMarkdownPreprocessor(unittest.TestCase):
    def testFile1(self):
        config = Config({
            'site_name': "HELLO WORLD!",
            "author": "Person 1"
        })
        markdown_preprocessor = MarkdownPreprocessor(config)
        output = markdown_preprocessor('tests/src/index.md')

        self.assertTrue(output['site_name'] == config.config['site_name'])
        self.assertTrue(output['author'] == config.config['author'])
        self.assertTrue(output['content'] is not None)


class TestConfig(unittest.TestCase):
    def test_load_from_file(self):
        config = Config.from_file(pathlib.Path('tests/src/config.json'))
        self.assertTrue(config.config == {
            "site_name": "Hello World!",
            "site_author": "Me!"
        })

    def test_overwrite(self):
        config = Config.from_file(pathlib.Path('tests/src/config.json'))
        input_dict = {"site_name": "New name!"}
        output = config(input_dict)
        self.assertTrue(output['site_name'] == input_dict['site_name'])
