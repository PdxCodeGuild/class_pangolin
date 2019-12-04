from django.db import models

# Create your models here.
class UrlPair(models.Model):
    
    code = models.CharField(max_length=200)
    long_url = models.CharField(max_length=400)
    