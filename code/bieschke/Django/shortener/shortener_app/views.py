from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Links

def redirect_view(request):
    return HttpResponse("Hello!")


def index(request):
    links = Links.objects.filter(created__lte=timezone.now()).order_by('created')
    return render(request, 'index.html', {'links':links})
    # return HttpResponse('<h1>Hello World Wide Web!</h1>')

def shorten(request):
    shorten_link = models.Links.shortencode
    return HttpResponseRedirect(reverse('shortener_app:index'))
