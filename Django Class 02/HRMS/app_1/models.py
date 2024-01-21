from django.db import models

# Create your models here.

class PersonModel(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)