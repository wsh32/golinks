from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Link(models.Model):
    long_link = models.CharField(max_length=200)
    short_link = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

