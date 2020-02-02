from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Event(models.Model):
    band = models.CharField(max_length=100, null='true')
    body = models.CharField(max_length=200)
    venue = models.CharField(max_length=100, null='true')
    street_address = models.CharField(max_length=100, null='true')
    city = models.CharField(max_length=100, null='true')
    state = models.CharField(max_length=100, null='true')
    date = models.CharField(max_length=100, null='true')
    time = models.CharField(max_length=100, null='true')
    price = models.CharField(max_length=100, null='true')
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
    null='true')
    image = models.ImageField(default='default.jpg', upload_to='locals_pics')
    url =models.URLField(blank=True)

    def __str__(self):
        return self.band

    
    