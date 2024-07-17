from github import Github

# # 设置你的GitHub Access Token，并确保它有足够的权限
# # 你可以在这里创建一个新的Token：https://github.com/settings/tokens
# access_token = ""
# github_Auth = ""
# githubHandler = ""
# # 设置你的PR数字和仓库信息
# owner = "Br1ze"  # 仓库拥有者的用户名
# repo = "Br1ze/MHP3"  # 仓库的名称
# pull_number = 1  # PR的编号

# 构建API请求的URL
# url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}"


# 获取 Pull Request 的基本信息
def get_pr_info(repo, pr_number, github_token):

    repoHandler = github_login(github_token, repo)

    pr_info = PrBasicInfoClass(repo, pr_number, "", "")

    pullRequest = repoHandler.get_pull(pr_number)

    pullRequestDescription = pullRequest.body

    pr_info.description = pullRequestDescription

    pullRequestTitle = pullRequest.title

    pr_info.title = pullRequestTitle

    last_commit = pullRequest.get_commits()[pullRequest.commits - 1]

    pullRequest.create_review_comment(
        "This is a new add comment", last_commit, "README.md", 1
    )

    return pr_info


# 登录GitHub
def github_login(github_token, repo):

    githubHandler = Github(github_token)
    repoHandler = githubHandler.get_repo(repo)

    return repoHandler


def get_pr_files(repo, pr_number, github_token):
    return ""


def comment_on_pr(repo, pr_number, comments, github_token):
    return ""


# Pull Request 基本信息的定义
class PrBasicInfoClass:
    def __init__(self, repo, prNumber, title, description):
        self._repo = repo
        self._prNumber = prNumber
        self._title = title
        self._description = description

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