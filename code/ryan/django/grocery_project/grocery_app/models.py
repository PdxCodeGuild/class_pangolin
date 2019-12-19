from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class GroceryItem(models.Model):
    content = models.CharField(max_length=200)
    date_created = models.DateTimeField(null=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.content
    