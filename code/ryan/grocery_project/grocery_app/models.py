from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class GroceryItem(models.Model):
    content = models.TextField()
    # date_created = models.DateTimeField(auto_now_add=True)