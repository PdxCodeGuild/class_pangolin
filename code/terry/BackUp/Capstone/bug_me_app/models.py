
from django.db import models

class Ticket(models.Model):
    title = models.CharField(max_length=200, blank=True, default="")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User', related_name='bug_me_app', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
    