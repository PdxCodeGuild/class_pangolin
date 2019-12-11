from django.shortcuts import get_list_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import ShortUrl

import random
import string
import re

def index(request):
    short_url = ''
    long_url = ShortUrl.objects
    context = {'short_url': short_url}
    # return HttpResponse("hello")
    return render(request, "url_shortner_app/index.html", context)

def user_input(request):
    print(request.POST)
    url_input = request.POST['long']
    look = request.META['REMOTE_ADDR']
    who = request.META['SERVER_NAME']
    characters = string.ascii_letters + string.digits + string.punctuation
    short_url= ""
    length = 5
    for n in range (length) :
        short_url += random.choice (characters)
    new = ShortUrl.objects.create(short_url= short_url,long_url= url_input, remote_addr=look, server_name=who)
    print(new.short_url, new.id)
    print(url_input)
    return HttpResponseRedirect(reverse('url_shortner_app:results', args=(short_url,)))

def results(request, short_url):
    # print(ShortUrl.objects.get(pk=pk))
    # return HttpResponseRedirect(reverse('url_shortner_app:long_text', args=(long_url,)))
    return render(request, "url_shortner_app/index.html", {'new_link': ShortUrl.objects.get(short_url=short_url)})

def redirect(request, short_url_param):
    new_url= ShortUrl.objects.get(short_url = short_url_param)
    if not re.match('(?:http|ftp|https)://', new_url.long_url):
        return HttpResponseRedirect('http://{}'.format(new_url.long_url))

    # print(new_url)
    return HttpResponseRedirect(new_url.long_url)
    



