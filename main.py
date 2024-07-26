import click
from gh.ghapi import get_pr_info
from gh.ghapi import comment_on_pr, comment_on_pr_by_line
from llm.llmapi import review_pr_code, summarize_pr_info


@click.group()
def cli():
    pass


@cli.command()
@click.option("-r", "--repo-name", required=True, help="The Repo to review")
@click.option("-n", "--pr-num", required=True, type=int, help="The PR number")
@click.option("--token", envvar="GH_TOKEN", help="Github token")
@click.option(
    "-g", "--guideline", required=False, type=str, help="The Path of guideline"
)
def summary(repo_name, pr_num, token, guideline):
    """Summarize a PR"""
    pr_info = get_pr_info(repo_name, pr_num, token, guideline)
    summary_result = summarize_pr_info(pr_info)
    comment_on_pr(repo_name, pr_num, token, summary_result)


@cli.command()
@click.option("-r", "--repo-name", required=True, help="The Repo to review")
@click.option("-n", "--pr-num", required=True, type=int, help="The PR number")
@click.option("--token", envvar="GH_TOKEN", help="Github token")
@click.option(
    "-g", "--guideline", required=False, type=str, help="The Path of guideline"
)
def review(repo_name, pr_num, token, guideline):
    """Review a PR"""
    pr_info = get_pr_info(repo_name, pr_num, token, guideline)
    code_review_result = review_pr_code(pr_info)
    feed_back = f"It's a {code_review_result.pr_type} PR, {code_review_result.summary}"
    comment_on_pr(repo_name, pr_num, token, feed_back)
    for inline_comment in code_review_result.comments:
        print(f"line_num_{inline_comment.line_num};{inline_comment.comment}")
        comment_on_pr_by_line(
            repo_name,
            pr_num,
            token,
            inline_comment.comment,
            inline_comment.relevant_file,
            inline_comment.line_num,
        )


if __name__ == "__main__":
    cli()
