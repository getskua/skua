import pathlib
import unittest

from skua.files import calculate_save_location, FindFilesByExtension


class TestFindFilesByExtension(unittest.TestCase):
    def test(self):
        file_finder = FindFilesByExtension(pathlib.Path('tests/src'))
        output = file_finder()
        expectation = ['tests/src/index.md', 'tests/src/blog/skua-is-a-static-site-generator.md',
                       'tests/src/blog/skua-is-still-a-static-site-generator.md', 'tests/src/blog/what-is-markdown.md',
                       'tests/src/blog/look-an-internal-link.md']
        self.assertTrue(len(list(output)) == len(expectation))
        for y in output:
            self.assertTrue(y in expectation)


class TestCalculateSaveLocation(unittest.TestCase):
    def test_root_source_directory(self):
        source_directory = pathlib.Path('test/input')
        output_directory = pathlib.Path('build/output')
        input_directory = ['test/input/collection/markdown_file.md', 'test/input/collection/another_markdown_file.md',
                           'test/input/collection2/markdown_file.md', 'test/input/collection2/another_markdown_file.md',
                           'test/input/collection3/markdown_file.md',
                           'test/input/collection3/another_markdown_file.md']
        output = [calculate_save_location(pathlib.Path(file), source_directory, output_directory) for file in
                  input_directory]
        expectation = ['build/output/collection/markdown_file.html',
                       'build/output/collection/another_markdown_file.html',
                       'build/output/collection2/markdown_file.html',
                       'build/output/collection2/another_markdown_file.html',
                       'build/output/collection3/markdown_file.html',
                       'build/output/collection3/another_markdown_file.html']

        for y, y_hat in zip(output, expectation):
            self.assertTrue(str(y) == y_hat)

    def test_middle_source_directory(self):
        source_directory = pathlib.Path('test/input')
        output_directory = pathlib.Path('build/output')
        input_directory = ['users/test/input/collection/markdown_file.md',
                           'users/test/input/collection/another_markdown_file.md',
                           'users/test/input/collection2/markdown_file.md',
                           'users/test/input/collection2/another_markdown_file.md',
                           'users/test/input/collection3/markdown_file.md',
                           'users/test/input/collection3/another_markdown_file.md']
        output = [calculate_save_location(pathlib.Path(file), source_directory, output_directory) for file in
                  input_directory]
        expectation = ['users/build/output/collection/markdown_file.html',
                       'users/build/output/collection/another_markdown_file.html',
                       'users/build/output/collection2/markdown_file.html',
                       'users/build/output/collection2/another_markdown_file.html',
                       'users/build/output/collection3/markdown_file.html',
                       'users/build/output/collection3/another_markdown_file.html']

        for y, y_hat in zip(output, expectation):
            self.assertTrue(str(y) == y_hat)
