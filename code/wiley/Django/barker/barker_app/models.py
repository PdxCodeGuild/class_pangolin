from django.db import models
from django.urls import reverse


class Bark(models.Model):
    body = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-created']
   
    def get_absolute_url(self):
        return reverse('barker_app:detail', args=(self.id,))
        