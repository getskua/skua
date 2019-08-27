import pathlib


class FindFilesByExtension(object):
    def __init__(self, source_directory: pathlib.Path = pathlib.Path("src"), extension="md"):
        self.source_directory: pathlib.Path = source_directory
        self.extension: str = extension

    def __call__(self, *args, **kwargs):
        return self.source_directory.glob('**/*.' + self.extension)


def calculate_save_location(file: pathlib.Path, source_directory: pathlib.Path,
                            output_directory: pathlib.Path) -> pathlib.Path:
    directory: pathlib.Path = file.parent
    start, stop = directory.parts.index(source_directory.parts[0]), directory.parts.index(source_directory.parts[-1])
    pre: pathlib.Path = pathlib.Path(''.join(directory.parts[:start]))
    post: pathlib.Path = pathlib.Path(''.join(directory.parts[stop + 1:]))
    return pathlib.Path(pre).joinpath(output_directory).joinpath(post).joinpath(file.parts[-1])
