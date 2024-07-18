import click
from gh.ghapi import get_pr_info
from gh.ghapi import get_pr_files
from gh.ghapi import comment_on_pr
from llm.llm import review_pr_code

@click.group()
def cli():
    pass

@cli.command()
@click.option('-r', '--repo-name', required=True, help='The Repo to review')
@click.option('-n', '--pr-num', required=True, type=int, help='The PR number')
@click.option('--token', envvar='GH_TOKEN', help='Github token')
def summary(repo_name,pr_num,token):
    """Summarize a PR"""
    get_pr_info(repo_name,pr_num,token)
    
@cli.command()
@click.option('-r', '--repo-name', required=True, help='The Repo to review')
@click.option('-n', '--pr-num', required=True, type=int, help='The PR number')
@click.option('--token', envvar='GH_TOKEN', help='Github token')
def review(repo_name,pr_num,token):
    """Review a PR"""
    click.echo(f"Review {repo_name}/{pr_num}/{token}")
    # Get the PR code files
    pr_files = get_pr_files(repo_name,pr_num,token)
    for pr_file in pr_files:
        filename = pr_file['filename']
        click.echo(f"Review file: {filename}")
        patch = pr_file['patch']
        for chunk in split_code_into_chunks(patch):
            review_response = review_pr_code(chunk)
            comment = f"**Review for {filename} (chunk):**\n\n{review_response}"
            click.echo(comment)
            comment_on_pr(repo_name, pr_num, comment, token)


def split_code_into_chunks(code, chunk_size=500):
    """
    Split a code string into chunks
    :param code: PR code patch
    :param chunk_size:  Chunk size
    """
    lines = code.split('\n')
    for i in range(0, len(lines), chunk_size):
        yield '\n'.join(lines[i:i + chunk_size])

if __name__ == '__main__':
    cli()