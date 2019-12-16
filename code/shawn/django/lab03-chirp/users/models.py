from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.dispatch import receiver
from posts.models import Chirp

# Create your models here.
class Profile(models.Model):
    headline = models.CharField(max_length=40, default="Hey you!")
    summary = models.CharField(max_length=250, default="Please click 'edit profile...' link below to get set up your profile.")
    picture = models.ImageField(upload_to='images/profiles/', default='images/profiles/default-profile.png')
    location = models.CharField(max_length=30, default="Please add a location.")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=12, default="Please add a first name.")
    last_name = models.CharField(max_length=15, default="Please add a last name.")
    
    users_followed = models.ManyToManyField('Profile', related_name='friends')
    chirps_liked = models.ManyToManyField(Chirp, related_name='likes')
    chirps_disliked = models.ManyToManyField(Chirp, related_name='dislikes')

    # to redirect after creating new 
    def get_absolute_url(self):
        return reverse('users:profile', args=(self.user.username,))

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()