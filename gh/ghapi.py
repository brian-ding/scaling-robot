from github import Github
from github import Auth
from gh.pr_info import PRInfo
import requests

# 获取 Pull Request 的基本信息
def get_pr_info(repo, pr_number, github_token, guideline):

    repoHandler = github_login(github_token, repo)

    pr_info = PRInfo(repo, pr_number, "", "", "", guideline)

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

def comment_on_pr(repo, pr_number, github_token,comments):
    repoHandler = github_login(github_token, repo)
    pullRequest = repoHandler.get_pull(pr_number)
    pullRequest.create_issue_comment(comments)
    comment_result = "Repo:%s pr_number: %d comment success." %(repo,pr_number)
    return comment_result

# Add comment into special code line.
# repo :  Repo name e.g. 'brian-ding/scaling-robot'
# pr_number: you can find pr_number in github
# github_token: your github token
# comments: the content of comment
# filePath: the file you want to add comments, e.g. "llm/llmapi.py"
# lineNumber: the line you want to add comments
def comment_on_pr_by_line(repo, pr_number, github_token,comments,filePath,lineNumber):
    repoHandler = github_login(github_token, repo)
    pullRequest = repoHandler.get_pull(pr_number)
    last_commit = pullRequest.get_commits()[pullRequest.commits - 1]
    pullRequest.create_comment(comments, last_commit, filePath, lineNumber)
    comment_result = "Repo:%s File: %s Line: %d comment success." %(repo,filePath,lineNumber)
    return comment_result

def read_url_data(url):
    response = requests.get(url)
    data = response.text
    return data