from django.db import models
from django.urls import reverse
from django.db import models

class Twitter(models.Model):
    title = models.CharField(max_length=140)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    my_image = models.ImageField(upload_to='avatar/', default='avatar/null.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.id,))
    
    class Meta:
        ordering = ['-created']