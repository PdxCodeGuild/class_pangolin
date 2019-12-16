import datetime

from django.db import models
from django.utils import timezone

class ShortURL(models.Model):
    inputURL = models.CharField(max_length=64)
    shortURL = models.CharField(max_length=12)
    ip = models.CharField(max_length=16)
    redirect = models.CharField(max_length=16)
    url_bits = models.IntegerField(default=0)

    def __str__(self):
        return self.inputURL

    def short(self):
        return self.shortURL