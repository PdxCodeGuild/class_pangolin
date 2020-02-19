
from django.db import models
# from .models import File

class Ticket(models.Model):
    title = models.CharField(max_length=200, blank=True, default="")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User', related_name='bug_me_app', on_delete=models.CASCADE)
    file = models.FileField(blank=True, null=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

class File(models.Model):
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.file.name