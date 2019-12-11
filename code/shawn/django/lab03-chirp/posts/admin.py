from django.contrib import admin

# Register your models here.
from .models import Chirp, Comment, Reaction
admin.site.register(Chirp)
admin.site.register(Comment)
admin.site.register(Reaction)
