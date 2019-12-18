from django.contrib import admin

# Register your models here.
from .models import Chirp, Comment
admin.site.register(Chirp)
admin.site.register(Comment)

