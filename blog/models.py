# from django.db import models
from djongo import models
from django.contrib.auth.models import AbstractUser
from modeltranslation.translator import register


class Post(models.Model):
    title = models.CharField(primary_key=True, max_length=1000)
    body = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    # Add custom fields here, e.g., profile picture, etc.
    # Example:
    # profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.username
