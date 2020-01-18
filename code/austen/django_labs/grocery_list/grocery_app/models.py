import datetime

from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):
    text_discription = models.CharField(max_length=200)
    created_date= models.DateTimeField('date created')
    completed_date= models.DateTimeField('date completed', null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    def __str__ (self):
        return self.text_discription


    # somewhere in the data base you should have this as a boolian
    # def was_it_completed(self):
    #     return self.completed_date 






# Create your models here.
