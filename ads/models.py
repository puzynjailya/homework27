from django.db import models
from uuid import uuid4


class Advertisement(models.Model):
    id = models.AutoField(editable=False, unique=True, primary_key=True, auto_created=True)
    name = models.CharField(max_length=150, null=True, blank=False)
    author = models.CharField(max_length=25,  null=True, blank=False)
    price = models.IntegerField( null=True, blank=False)
    description = models.CharField(max_length=3000, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=False)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, unique=True, primary_key=True, auto_created=True)
    name = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name
