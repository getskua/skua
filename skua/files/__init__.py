import pathlib


class FindFilesByExtension(object):
    def __init__(self, source_directory: pathlib.Path = pathlib.Path("src"), extension="md"):
        self.source_directory: pathlib.Path = source_directory
        self.extension: str = extension

    def __call__(self, *args, **kwargs):
        return self.source_directory.glob('**/*.' + self.extension)


def calculate_save_location(file: pathlib.Path, source_directory: pathlib.Path,
                            output_directory: pathlib.Path, output_format: str = 'html') -> pathlib.Path:
    """
    Calculates where a file should be saved.
    :param file: A pathlib.Path object pointing to the file.
    :param source_directory: Where all the source files are stored.
    :param output_directory: Where all the HTML fies should be placed.
    :param output_format: The extension for the save location.
    :return:
    """
    directory: pathlib.Path = file.parent
    start, stop = directory.parts.index(source_directory.parts[0]), directory.parts.index(source_directory.parts[-1])
    pre: pathlib.Path = pathlib.Path(''.join(directory.parts[:start]))
    post: pathlib.Path = pathlib.Path(''.join(directory.parts[stop + 1:]))
    return pathlib.Path(pre).joinpath(output_directory).joinpath(post).joinpath(
        file.stem + '.' + output_format)
