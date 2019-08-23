import unittest

from skua.files import generate_output_filenames, generate_sparse_index, generate_detailed_index


class TestOutputFilenameGenerator(unittest.TestCase):
    def testNoNesting(self):
        output = generate_output_filenames(
            ['src/index.md', 'src/blog/skua-is-a-static-file-generator.md', 'src/LICENSE.md'],
            'src', 'build')
        expectation = ['build/index.md', 'build/blog/skua-is-a-static-file-generator.md', 'build/LICENSE.md']
        for (y_hat, y) in zip(output, expectation):
            self.assertTrue(y_hat == y)

    def testNesting(self):
        output = generate_output_filenames(
            ['project/docs/src/index.md', 'project/docs/src/blog/skua-is-a-static-file-generator.md',
             'project/docs/src/LICENSE.md'],
            'src', 'build')
        expectation = ['project/docs/build/index.md', 'project/docs/build/blog/skua-is-a-static-file-generator.md',
                       'project/docs/build/LICENSE.md']
        for (y_hat, y) in zip(output, expectation):
            self.assertTrue(y_hat == y)


class TestSparseIndex(unittest.TestCase):
    def test1(self):
        output = generate_sparse_index('tests/src/blog')
        expectation = ['tests/src/blog/skua-is-still-a-static-site-generator.md', 'tests/src/blog/what-is-markdown.md',
                       'tests/src/blog/skua-is-a-static-site-generator.md']
        for (y_hat, y) in zip(output, expectation):
            self.assertTrue(y_hat == y)


class TestDetailedIndex(unittest.TestCase):
    def test2(self):
        output = generate_detailed_index('tests/src/blog')
        expectation = [{'template': 'skua_blogpost', 'publish_date': '22/08/2019', 'publish_time': '14:55:11 UTC',
                        'title': 'Hello World!', 'subtitle': 'I exist!'},
                       {'template': 'skua_blogpost', 'publish_date': '22/08/2019', 'publish_time': '15:33:00 UTC',
                        'title': 'Hello World!', 'subtitle': 'I exist!'},
                       {'template': 'skua_blogpost', 'publish_date': '19/08/2019', 'publish_time': '12:01:00 UTC',
                        'title': 'Hello World!', 'subtitle': 'I exist!'}]

        for (y_hat, y) in zip(output, expectation):
            self.assertTrue(y_hat == y)
