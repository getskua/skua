import unittest

from skua.files import generate_output_filenames


class TestOutputFilenameGenerator(unittest.TestCase):
    def test_no_nesting(self):
        output = generate_output_filenames(
            ['src/index.md', 'src/blog/skua-is-a-static-file-generator.md', 'src/LICENSE.md'],
            'src', 'build')
        expectation = ['build/index.md', 'build/blog/skua-is-a-static-file-generator.md', 'build/LICENSE.md']
        for (y_hat, y) in zip(output, expectation):
            self.assertTrue(y_hat == y)

    def test_nesting(self):
        output = generate_output_filenames(
            ['project/docs/src/index.md', 'project/docs/src/blog/skua-is-a-static-file-generator.md',
             'project/docs/src/LICENSE.md'],
            'src', 'build')
        expectation = ['project/docs/build/index.md', 'project/docs/build/blog/skua-is-a-static-file-generator.md',
                       'project/docs/build/LICENSE.md']
        list(output)
        for (y_hat, y) in zip(output, expectation):
            self.assertTrue(y_hat == y)
