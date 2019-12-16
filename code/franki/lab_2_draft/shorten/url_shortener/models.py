from django.db import models
from .utils import code_generator, create_shortcode 

class Abbreviation(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=6, unique=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(Abbreviation, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)