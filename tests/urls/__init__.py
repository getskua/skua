import pathlib
import unittest

from skua.urls import path2url


class TestPath2Url(unittest.TestCase):
    def test1(self):
        inputs = [pathlib.Path('src/blog/skua-is-a-static-site-generator.md')]
        outputs = [path2url(path, 'https://example.com') for path in inputs]
        expectation = ['https://example.com/blog/skua-is-a-static-site-generator.html']
        for y, y_hat in zip(expectation, outputs):
            self.assertTrue(y == y_hat)
