import pathlib


def path2url(file: pathlib.Path, site_url: str, output_directory: pathlib.Path = pathlib.Path('src')) -> str:
    """
    Converts a path into a website URL.
    :param file:
    :param site_url:
    :param output_directory:
    :return:
    """
    stop = file.parts.index(output_directory.parts[-1])
    return site_url + '/' + '/'.join(file.parts[stop+1:])
