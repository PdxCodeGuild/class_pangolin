from django.db import models

class GroceryEntry(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField()
    completion_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name