import datetime
import random
import string #set of all ascii characters
from django.utils import timezone
from django.db import models

def code_generator(size=6, chars=(string.ascii_lowercase + string.digits)):
    return ''.join(random.choice(chars) for x in range(size))

class Links(models.Model):

    link = models.URLField(max_length=500)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    hits = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)

    def save(self):
        self.shortcode = code_generator() 
        self.created = timezone.now()
        super(Links, self).save()

    def __str__(self):
        return self.link

    def __unicode__(self):
        return str(self.url)    

'''
every time you update your models, 
python3 manage.py makemigrations
python3 manage.py migrate
'''