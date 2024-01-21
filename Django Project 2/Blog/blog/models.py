from django.db import models
from django.contrib.auth.models import User

class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
