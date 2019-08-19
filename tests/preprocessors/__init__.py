import unittest

from skua.preprocessors import Config
from skua.preprocessors.markdown import MarkdownPreprocessor


class TestMarkdownPreprocessor(unittest.TestCase):
    def testFile1(self):
        config = Config({
            'site_name': "HELLO WORLD!",
            "author": "Person 1"
        })
        import os
        markdown_preprocessor = MarkdownPreprocessor(config)
        output = markdown_preprocessor('tests/src/index.md')

        self.assertTrue(output['site_name'] == config.config['site_name'])
        self.assertTrue(output['author'] == config.config['author'])
        self.assertTrue(output['content'] is not None)
