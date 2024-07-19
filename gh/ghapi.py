from github import Github
from github import Auth
from gh.pr_info import PRInfo
import requests

# 获取 Pull Request 的基本信息
def get_pr_info(repo, pr_number, github_token):

    repoHandler = github_login(github_token, repo)

    pr_info = PRInfo(repo, pr_number,"","","")

    pullRequest = repoHandler.get_pull(pr_number)

    pr_info.description = pullRequest.body

    pr_info.title = pullRequest.title

    pr_info.diff = read_url_data(pullRequest.diff_url)

    return pr_info


# 登录GitHub
def github_login(github_token, repo):

    githubHandler = Github(github_token)
    repoHandler = githubHandler.get_repo(repo)

    return repoHandler


# 使用user的token 登录GitHub
def github_user_login(github_user_token, repo):

    github_Auth = Auth.Token(github_user_token)
    githubHandler = Github(auth=github_Auth)
    githubHandler = Github(github_user_token)
    repoHandler = githubHandler.get_repo(repo)
    return repoHandler



def get_pr_files(repo, pr_number, github_token):
    return ""


def comment_on_pr(repo, pr_number, github_token,comments):
    repoHandler = github_login(github_token, repo)
    pullRequest = repoHandler.get_pull(pr_number)
    pullRequest.create_issue_comment(comments)
    return "comment success."


 
def read_url_data(url):
    response = requests.get(url)
    data = response.text
    return data