from django.db import models
from django.urls import reverse
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)       #this will be now() when created
    updated = models.DateTimeField(auto_now=True)           #this will be now() whenever the model is updated/modified
    body = models.TextField()
    
    def __str__(self):
        return self.title

    # this is used for the CreateView class based view, so that it knows where to redirect in case the view 
    # gets a POST request instead of a GET
    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.id,))

    class Meta:
        ordering = ['-created']