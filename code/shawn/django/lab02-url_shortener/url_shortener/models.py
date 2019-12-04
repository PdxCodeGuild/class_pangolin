from django.db import models

# Create your models here.
class UrlPair(models.Model):
    
    # short and long URLs
    code = models.CharField(max_length=200)
    long_url = models.CharField(max_length=400)

class Hit(models.Model):

    # metadata
    ip_address = models.CharField(max_length=48)    
    host_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    # urlpair foreign key
    urlpair_key = models.ForeignKey(UrlPair, on_delete=models.CASCADE)
    
