# from django.db import models
from djongo import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(primary_key=True, max_length=1000)
    body = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.title
