from email.mime import image
from statistics import mode
from unicodedata import category
from django.db import models


class Pubicaciones(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='fotos', null=True, blank= True)
    description = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title