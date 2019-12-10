from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Links
from django.http import HttpResponse

def index(request):
    links = Links.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'shortener_app/index.html', {'links':links})
    # return HttpResponse('<h1>Hello World Wide Web!</h1>')

def shorten(request):
    shorten_link = models.Links.shorten.link
    return HttpResponseRedirect(reverse('shorten_app:index'))


def lengthen(request):
    lengthen_link = models.Links.lengthen.link
    return HttpResponseRedirect(reverse('shorten_app:index'))

    