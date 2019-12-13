from django import forms 
from .models import ShortUrl
 
class UrlForm(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = ['long_url']