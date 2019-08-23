import re

from git import Repo


class Git(object):
    def __init__(self, working_dir='./'):
        self.working_dir = working_dir
        self.repo = Repo(working_dir)

    def find_changes(self, filetype='md'):
        return [item.a_path for item in self.repo.index.diff(None) if re.search('.' + filetype, item.a_path)]
