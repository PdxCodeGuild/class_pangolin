from django.shortcuts import render, redirect
from django.views import View
from .models import ShortUrl
from .forms import  UrlForm
from .shortener import Shortener



def Make(request):
    form = UrlForm(request.POST)
    a = ""
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = Shortener().issue_token()
            NewUrl.short_url = a
            NewUrl.save()
        else:
            form = UrlForm()
            a = "Invalid URL"
    return render(request, 'home.html', {'form': form, 'a': a})

def Home(request, token):
    long_url = ShortUrl.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)