from django.db import models
from django.urls import reverse

class Chirp(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=320)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/chirps/', null=True, blank=True)

    def __str__(self):
        return f"{self.author} chirped at {self.date_created}"

    # to make it show items in chronological order
    class Meta:
        ordering = ['-date_created']

    # to redirect after creating new 
    def get_absolute_url(self):
        return reverse('posts:home')

class Comment(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=240)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    chirp = models.ForeignKey(Chirp, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} commented at {self.date_created}"

    # to make it show items in chronological order
    class Meta:
        ordering = ['-date_created']

class Reaction(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    reaction = models.CharField(max_length=4)                           # like, love, hate, mad?
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)   # link it back to the author
    chirp = models.ForeignKey(Chirp, on_delete=models.CASCADE)          # link it back to chirp

    def __str__(self):
        return f"{self.author} -- {self.reaction}"

class Follow(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    follower = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="user_thats_following")
    followee = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="user_being_followed")