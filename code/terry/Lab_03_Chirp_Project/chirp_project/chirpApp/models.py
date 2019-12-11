from django.db import models
from django.urls import reverse

class Chirp(models.Model):
    author = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    body_text = models.TextField(max_length=128)

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('chirpApp:detail', args=(self.id,))



