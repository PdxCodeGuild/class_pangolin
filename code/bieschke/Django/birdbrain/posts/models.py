from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    brain = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    peekchure = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        # return self.brain         Don't make mandatory model fields optional, otherwise your code will break
        return f"{self.author} -- {self.id}"

    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.id,))

    def clean(self):
        # Picture or brain or both must be present.
        if not self.brain and not self.peekchure:
            raise ValidationError(_('You must have a picture or a brain'))
        