from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField(null=True)
    is_married = models.BooleanField(null=True)
    kids = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
