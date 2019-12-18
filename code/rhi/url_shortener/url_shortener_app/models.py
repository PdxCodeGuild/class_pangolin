from django.db import models
from django.utils import timezone

# Create your models here.
class Urls(models.Model):
    short_id = models.SlugField(max_length=6, primary_key=True)
    httpurl = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)
    ip_orig = models.CharField(max_length=50, default='Null')

    def __str__(self):
        return self.httpurl