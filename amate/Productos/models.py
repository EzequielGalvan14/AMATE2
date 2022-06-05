from email.mime import image
from statistics import mode
from unicodedata import category
from django.db import models

# Create your models here.

class producto(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='productos', null=True, blank= True)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=30)
    active = models.BooleanField(default=True)