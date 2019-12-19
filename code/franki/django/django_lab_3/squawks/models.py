from django.db import models
from django.urls import reverse

class Squawk(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=240)

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('squawks:detail', args=(self.id,))
