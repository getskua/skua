import pathlib

import yaml


class GlobalConfig:
    def __init__(self, path: pathlib.Path = pathlib.Path("config.yml")):
        if not path.exists():
            raise FileNotFoundError("The file 'config.yml' does not exist!")
        self.config_file = path.open('r')
        self.parsed_yaml = yaml.parse(self.config_file)
