import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('-r', '--repo-name', required=True, help='The Repo to review')
@click.option('-n', '--pr-num', required=True, type=int, help='The PR number')
@click.option('--token', envvar='GH_TOKEN', help='Github token')
def review(repo_name,pr_num,token):
    """Review a PR"""
    click.echo(f"Reviewing {repo_name}/{pr_num}/{token}")

@cli.command()
@click.option('-r', '--repo-name', required=True, help='The Repo to review')
@click.option('-n', '--pr-num', required=True, type=int, help='The PR number')
@click.option('--token', envvar='GH_TOKEN', help='Github token')
def summary(repo_name,pr_num,token):
    """Summarize a PR"""
    click.echo(f"Summarizing {repo_name}/{pr_num}/{token}")
    
if __name__ == '__main__':
    cli()