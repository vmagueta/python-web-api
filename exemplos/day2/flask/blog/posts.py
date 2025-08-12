from blog.database import mongo
from datetime import datetime
from unidecode import unidecode


def get_all_posts(published: bool = True):
    """Get all blog posts order by date."""
    posts = mongo.db.posts.find({"published": True})
    return posts.sort("date")


def get_post_by_slug(slug: str) -> dict:
    """\
    Get a blog post by its slug.

    ex. 
    /Novidades%20de%202025
    /Novidades de 2025
    /novidades-de-2025
    """
    post = mongo.db.posts.find_one({"slug": slug})
    return post


def update_post_by_slug(slug: str, data: dict) -> dict:
    """Update a blog post by its slug."""
    # TODO: Se o titulo mudar, atualizar o slug (falhar se ja existir)
    return mongo.db.posts.find_one_and_update({"slug": slug}, {"$set": data})


def new_post(title: str, content: str, published: bool = True) -> str:
    """Create a new blog post and returns a slug."""
    slug = unidecode(title.replace(" ", "-").replace("_", "-").lower())
    # TODO: Verificar se post com este slug ja existe
    mongo.db.posts.insert_one(
        {
            "title": title,
            "content": content,
            "published": published,
            "slug": slug,
            "date": datetime.now(),
        }
    )
    return slug


def delete_post(slug):
    """Delete a post for db."""
    mongo.db.posts.delete_one({"slug": slug})
    return f"Post {slug} deleted."
