import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class GroceryItem(models.Model):
    text_description = models.CharField(max_length=50)
    date_created = models.DateTimeField('date created')
    date_completed = models.DateTimeField('date completed', null=True, blank=True)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.text_description
    def was_created_recently(self):
        return self.date_created >= timezone.now() - datetime.timedelta(days=3)
    def was_completed_recently(self):
        return self.date_completed >= timezone.now() - datetime.timedelta(days=3)