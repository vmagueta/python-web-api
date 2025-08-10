import click

from blog.posts import (
    new_post, 
    get_all_posts, 
    get_post_by_slug, 
    update_post_by_slug
)


@click.group()
def post():
    """\
    Manage blog posts in CLI.

    Commands:
    - new: Create a new blog post
    - list: List all blog posts
    - get: Get a blog post by slug
    - update: Update a blog post by slug
    """


@post.command()
@click.option("--title")
@click.option("--content")
def new(title, content):
    """Add new post to database."""
    new_post(title, content)
    click.echo(f"New post created {new}.")


@post.command("list")
def _list():
    """List all blog posts."""
    posts = get_all_posts()
    for post in posts:
        click.echo(post)
        click.echo("-" * 30)


@post.command()
@click.argument("slug")
def get(slug):
    """Get a blog post by slug."""
    post = get_post_by_slug(slug)
    click.echo(post or "post not found")


@post.command()
@click.argument("slug")
@click.option("--content", default=None, type=str)
@click.option("--published", default=None, type=str)
def update(slug, content, published):
    """Update a blog post by slug."""
    data = {}
    if content is not None:
        data["content"] = content
    if published is not None:
        data["published"] = published.lower() == "true"
    update_post_by_slug(slug, data)
    click.echo("Post updated")


# TODO: Criar comando para deletar ou despublicar posts


def configure(app):
    """Configure the post commands."""
    app.cli.add_command(post)
