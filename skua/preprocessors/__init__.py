import json
import pathlib


class Config(object):
    def __init__(self, config: dict):
        self.config: dict = config

    def __call__(self, file_dict) -> dict:
        # config keys overwrite the keys specified in the file
        return {**file_dict, **self.config}

    def __len__(self):
        return len(self.config)

    @classmethod
    def from_file(cls, file: pathlib.Path):
        opened_file = file.open()
        val = cls(json.load(opened_file))
        opened_file.close()
        return val


class Preprocessor(object):
    def __init__(self, config: Config):
        self.config = config

    def preprocess(self, *args, **kwargs) -> dict:
        pass

    def __call__(self, input_file) -> dict:
        return self.config(self.preprocess(input_file))
