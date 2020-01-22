from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    pet = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(
        default='default.jpg', upload_to='pet_pics'
    )

    def __str__(self):
        return f'{self.animals.animalName}'
