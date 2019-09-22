import pathlib
import unittest

from skua.files import calculate_save_location, FindFilesByExtension, generate_index, copy_files


class TestGenerateIndex(unittest.TestCase):
    def test_not_recursive(self):
        outputs = generate_index(pathlib.Path('tests/src/blog'))
        expectations = [{'template': 'skua_blogpost', 'publish_date': '22/08/2019', 'publish_time': '14:55:11 UTC',
                         'title': 'Hello World!', 'subtitle': 'I exist!',
                         'file_path': pathlib.PosixPath('tests/src/blog/skua-is-still-a-static-site-generator.md'),
                         'content': '# Skua remains a static site generator\n(No surprises here!)\n\n**This site is '
                                    'for testing purposes (hence the gibberish content)!**'},
                        {'template': 'skua_blogpost', 'publish_date': '22/08/2019', 'publish_time': '15:33:00 UTC',
                         'title': 'Hello World!', 'subtitle': 'I exist!',
                         'file_path': pathlib.PosixPath('tests/src/blog/what-is-markdown.md'),
                         'content': '# Markdown is a markup language\n(No surprises here)\n\n**This site is for '
                                    'testing purposes (hence the gibberish content)!**'},
                        {'template': 'skua_blogpost', 'publish_date': '19/08/2019', 'publish_time': '12:01:00 UTC',
                         'title': 'Hello World!', 'subtitle': 'I exist!',
                         'file_path': pathlib.PosixPath('tests/src/blog/skua-is-a-static-site-generator.md'),
                         'content': '# Skua is a static site generator\n(No surprises here)\n\n**This site is for '
                                    'testing purposes (hence the gibberish content)!**'},
                        {'template': 'skua_blogpost', 'publish_date': '19/08/2019', 'publish_time': '12:01:00 UTC',
                         'title': 'Hello World!', 'subtitle': 'I exist!',
                         'file_path': pathlib.PosixPath('tests/src/blog/look-an-internal-link.md'),
                         'content': '[Link](tests/src/blog/skua-is-a-static-site-generator.md)'}]

        self.assertTrue(len(expectations) == len(list(outputs)))
        outputs = generate_index(pathlib.Path('tests/src/blog'))
        for output in outputs:
            self.assertTrue(output in expectations)

    def test_recursive(self):
        index = generate_index(pathlib.Path('tests/src/blog'), recursive=True)
        expectations = [{'template': 'skua_blogpost', 'publish_date': '22/08/2019', 'publish_time': '14:55:11 UTC',
                         'title': 'Hello World!', 'subtitle': 'I exist!',
                         'file_path': pathlib.PosixPath('tests/src/blog/skua-is-still-a-static-site-generator.md')},
                        {'template': 'skua_blogpost', 'publish_date': '22/08/2019', 'publish_time': '15:33:00 UTC',
                         'title': 'Hello World!', 'subtitle': 'I exist!',
                         'file_path': pathlib.PosixPath('tests/src/blog/what-is-markdown.md')},
                        {'template': 'skua_blogpost', 'publish_date': '19/08/2019', 'publish_time': '12:01:00 UTC',
                         'title': 'Hello World!', 'subtitle': 'I exist!',
                         'file_path': pathlib.PosixPath('tests/src/blog/skua-is-a-static-site-generator.md')},
                        {'template': 'skua_blogpost', 'publish_date': '19/08/2019', 'publish_time': '12:01:00 UTC',
                         'title': 'Hello World!', 'subtitle': 'I exist!',
                         'file_path': pathlib.PosixPath('tests/src/blog/look-an-internal-link.md')}]


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


class TestCopyFiles(unittest.TestCase):
    def test(self):
        copy_files(pathlib.Path('tests/src/'), pathlib.Path('tests/build'), extensions=['yml'],
                   recursive=True)
