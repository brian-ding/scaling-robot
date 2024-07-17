import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('-r', '--repo-name', required=True, help='The Repo to review')
@click.option('-n', '--pr-num', required=True, type=int, help='The PR number')
def review(repo_name,pr_num):
    """Review a PR"""
    click.echo(f"Reviewing {repo_name}/{pr_num}")

@cli.command()
@click.option('-r', '--repo-name', required=True, help='The Repo to review')
@click.option('-n', '--pr-num', required=True, type=int, help='The PR number')
def summary(repo_name,pr_num):
    """Summarize a PR"""
    click.echo(f"Summarizing {repo_name}/{pr_num}")
    
if __name__ == '__main__':
    cli()