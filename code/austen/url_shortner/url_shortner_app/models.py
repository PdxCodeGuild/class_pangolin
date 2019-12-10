from django.db import models


# Create your models here.
class ShortUrl(models.Model):
    short_url = models.URLField(max_length= 200)
    long_url = models.URLField(max_length= 200)
    remote_addr = models.CharField(max_length= 100, null=True, blank=True)
    server_name = models.CharField(max_length= 100, null=True, blank=True)

    def __str__(self):
        return self.short_url