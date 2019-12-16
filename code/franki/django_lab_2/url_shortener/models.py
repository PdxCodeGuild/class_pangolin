from django.db import models

class ShortUrl(models.Model):
    long_url = models.URLField("URL", unique=True)
    short_url = models.CharField(max_length=6)
