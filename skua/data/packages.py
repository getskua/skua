import git


class RemotePackage:
    def __init__(self, url: str, name: str, download: bool = True):
        self.repo = git.Repo.clone_from(url, to_path=name)


class LocalPackage:
    def __init__(self, path):
        self.path = path
