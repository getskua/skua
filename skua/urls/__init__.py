import pathlib
from typing import Iterable

from bs4 import BeautifulSoup

def path2url(file: pathlib.Path, site_url: str, source_directory: pathlib.Path = pathlib.Path('src'),
             output_format: str = 'html') -> str:
    """
    Converts a path into a web address. Strips everything up to and including the source directory from the path and
    then concatenates that stripped down path to the website url.

    :param output_format: The extension for output files (normally '.html').

    :param file: A pathlib.Path object pointing to hte input file.

    :param site_url: The url of the website, not including a leading slash (so `https://example.com` NOT
    `https://example.com/`.

    :param source_directory: Where all the files are stored.
    :return:
    """
    stop = file.parts.index(source_directory.parts[-1])
    return site_url + '/' + '/'.join(file.parts[stop + 1:-1]) + '/' + file.stem + '.' + output_format
