class Preprocessor(object):
    def __init__(self):
        pass

    def preprocess(self, *args, **kwargs):
        pass

    def __call__(self, input_file):
        return self.preprocess(input_file)
