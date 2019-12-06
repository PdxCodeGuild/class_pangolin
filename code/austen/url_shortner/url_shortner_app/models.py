from django.db import models


# Create your models here.
class ShortUrl(models.Model):
    short_url = models.URLField(max_length= 200)
    long_url = models.URLField(max_length= 200)
    is_converted = models.BooleanField(default=False)
    def __str__(self):
        return self.short_url