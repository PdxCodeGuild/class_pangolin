import datetime

from django.utils import timezone
from django.db import models

# Create your models here.

class GroceryItem(models.Model):
  title = models.CharField(max_length=200)
  description = models.CharField(max_length=500, null=True, blank=True)
  created_date = models.DateTimeField(default=timezone.now) 
  completed_date = models.DateTimeField(null=True, blank=True) 
  completed = models.BooleanField(default=False)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
        return self.title