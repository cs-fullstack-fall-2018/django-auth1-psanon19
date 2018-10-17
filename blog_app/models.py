from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class BlogModel(models.Model):
    blog_title = models.CharField(max_length=500)
    blog_entry = models.TextField(max_length=1000)
    dateCreated = models.DateTimeField(default=datetime.now)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.blog_title
