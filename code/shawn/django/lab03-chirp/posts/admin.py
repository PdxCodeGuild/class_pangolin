from django.contrib import admin

# Register your models here.
from .models import Chirp, Comment, Reaction, Follow
admin.site.register(Chirp)
admin.site.register(Comment)
admin.site.register(Reaction)
admin.site.register(Follow)
