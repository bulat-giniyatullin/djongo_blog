import os
import django
from blog.models import Post


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_djongo.settings")
django.setup()


def create_posts():
    # Create posts here
    Post.objects.create(title="Post 1", body="Content of Post 1")
    Post.objects.create(title="Post 2", body="Content of Post 2")
    Post.objects.create(title="Post 3", body="Content of Post 3")
    Post.objects.create(title="Post 4", body="Content of Post 4")


if __name__ == "__main__":
    create_posts()
