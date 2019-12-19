from django.contrib import admin
from url_shortener_app.models import Urls

# Register your models here.

class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'httpurl', 'pub_date', 'count')
    ordering = ('-pub_date',)
    
# register the Urls model with UrlsAdmin options
admin.site.register(Urls, UrlsAdmin)