import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class LongUrl(models.Model):
    url_text = models.CharField(max_length=500)
    tiny_text = models.CharField(max_length=20)
    IPs = models.CharField(max_length=30, blank=True, null=True)
    redirectIP = models.CharField(max_length=30, blank=True, null=True)
    url_bits = models.IntegerField(default=0, blank=True, null=True)
    def __str__(self):
        return self.url_text

    def showtiny(self):
        return self.tiny_text
