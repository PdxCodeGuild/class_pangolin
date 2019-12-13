from django.db import models
import random
class Abbreviation(models.Model):
    long_url = models.CharField(max_length=220)
    short_url = models.CharField(max_length=6, unique=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs)
        print('something')
        super(Abbreviations, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.long_url)