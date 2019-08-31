import pathlib
import unittest

from skua.preprocessors.markdown import MarkdownPreprocessor
from skua.render import Templates
from skua.urls import path2url, transform_links


class TestPath2Url(unittest.TestCase):
    def test1(self):
        inputs = [(pathlib.Path('src/blog/skua-is-a-static-site-generator.md'), 'src'),
                  (pathlib.Path('src/second_src/file.md'), pathlib.Path('src/second_src'))]
        outputs = [path2url(path[0], 'https://example.com', output_directory=pathlib.Path(path[1])) for path in inputs]
        expectation = ['https://example.com/blog/skua-is-a-static-site-generator.md', 'https://example.com/file.md']
        for y, y_hat in zip(expectation, outputs):
            self.assertTrue(y == y_hat)


class TestTransformLinks(unittest.TestCase):
    def test2(self):
        md_preprocessor = MarkdownPreprocessor()
        templates = Templates(pathlib.Path('tests/src/templates'))
        output = templates.render_template(**md_preprocessor(pathlib.Path('tests/src/blog/look-an-internal-link.md')))
        output = transform_links(output, 'https://example.com', output_directory=pathlib.Path('tests/src'))