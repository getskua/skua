import unittest

from skua.files import generate_output_filenames


class TestOutputFilenameGenerator(unittest.TestCase):
    def test1(self):
        output = generate_output_filenames(
            ['src/index.md', 'src/blog/skua-is-a-static-file-generator.md', 'src/LICENSE.md'],
            'src', 'build')
        expectation = ['build/index.md', 'build/blog/skua-is-a-static-file-generator.md', 'build/LICENSE.md']
        for (y_hat, y) in zip(output, expectation):
            self.assertTrue(y_hat == y)
