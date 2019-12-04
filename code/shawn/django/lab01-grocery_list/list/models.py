from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    description_text = models.CharField(max_length = 200)
    created_date = models.DateTimeField('date created')
    completed_date = models.DateTimeField('date completed', null=True, blank=True)
    is_completed = models.BooleanField(default=False)