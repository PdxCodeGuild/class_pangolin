from django.db import models
from django.utils import timezone 

class GroceryItem(models.Model):
    content = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    date_completed = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name