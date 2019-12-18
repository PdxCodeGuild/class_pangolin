from django.db import models

# Create your models here.
class UrlShortener(models.Model):
    long_url = models.CharField(max_length=200)
    short = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.long_url

    def __str__(self):
        return self.short
    