# This is gh/pr_info.py

class PRInfo:
    def __init__(self, repo, prNumber, title, description, diff):
        self._repo = repo
        self._prNumber = prNumber
        self._title = title
        self._description = description
        self._diff = diff

    # Get & Set for Repo info
    @property
    def repo(self):
        return self._repo

    @repo.setter
    def repo(self, repo):
        self._repo = repo

    # Get & Set for Pull Request Number
    @property
    def prNumber(self):
        return self._prNumber

    @prNumber.setter
    def prNumber(self, prNumber):
        self._prNumber = prNumber

    # Get & Set for Title info
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    # Get & Set for description
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description
        

    # Get & Set for change info
    @property
    def diff(self):
        return self._diff

    @diff.setter
    def diff(self, diff):
        self._diff = diff