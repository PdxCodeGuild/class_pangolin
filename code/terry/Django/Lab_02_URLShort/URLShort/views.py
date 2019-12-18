import string
import random

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import ShortURL

def index(request, shortURL=''):
    context = {'shortURL':shortURL}
    return render(request, 'URLShort/index.html', context)

def short(request):
    userInput = request.POST['user_url']
    location = request.META['REMOTE_ADDR']
    user_length = request.META['CONTENT_LENGTH']
    print(f"User IP is {location}")
    chars = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(6))
    toSave = ShortURL.objects.create(inputURL = userInput, shortURL = chars, ip = location, url_bits = user_length)
    return HttpResponseRedirect(reverse('URLShort:index_with_short', args=(toSave.shortURL,)))

def redirect(request, shortURL):
    get_long = ShortURL.objects.get(shortURL = shortURL)
    goto_IP = request.META['REMOTE_ADDR']
    get_long.redirectIP = goto_IP
    get_long.save()
    print(f"Redirecting to {get_long}")
    return HttpResponseRedirect(get_long.inputURL)