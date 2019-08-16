class Config(object):
    def __init__(self, config: dict):
        self.config: dict = config

    def __call__(self, file_dict) -> dict:
        # config keys overwrite the keys specified in the file
        return {**file_dict, **self.config}


class Preprocessor(object):
    def __init__(self, config: Config):
        self.config = config

    def preprocess(self, *args, **kwargs) -> dict:
        pass

    def __call__(self, input_file) -> dict:
        return self.config(self.preprocess(input_file))
