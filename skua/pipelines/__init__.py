from typing import Callable, List

from skua.render import Templates


class Pipeline(object):
    def __init__(self, *args):
        self.pipeline: List[Callable] = list(args)

    def __call__(self, file):
        for step in self.pipeline:
            if isinstance(step, Templates):
                file = step(**file)
            else:
                file = step(file)
        return file