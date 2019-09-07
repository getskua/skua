import pathlib

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
    intermediate = '/'.join(file.parts[stop + 1:-1])
    extra = '/' if len(intermediate) > 0 else ''
    return site_url + '/' + intermediate + extra + file.stem + '.' + output_format


def transform_links(output_file, site_url, source_directory=pathlib.Path('tests/src')):
    soup = BeautifulSoup(output_file, 'html.parser')
    for a in soup.find_all('a'):
        link = pathlib.Path(a['href'])
        index = link.parts.index(source_directory.parts[-1])
        link = site_url + '/' + '/'.join(link.parts[index + 1:])
        a['href'] = link
    return str(soup)
