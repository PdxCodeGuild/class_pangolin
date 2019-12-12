from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import random
import string
from .models import LongUrl

# Create your views here.
def index(request, tiny_text=''):
    context = {
        'tiny_text': tiny_text,
    }
    return render(request, 'tinyurl_app/index.html', context)

def shorten(request):
    user_input = request.POST['user_url']
    location = request.META['REMOTE_ADDR']
    user_length = request.META['CONTENT_LENGTH']
    print(f"User IP address is {location}")
    shorten_call = ''.join(random.choice(string.ascii_letters) for i in range(5))
    var = LongUrl.objects.create(url_text = user_input, tiny_text=shorten_call, IPs = location, url_bits=user_length)
    return HttpResponseRedirect(reverse('tinyurl_app:index_with_short', args=(var.tiny_text,)))

def redirecting(request, tiny_text):
    get_long = LongUrl.objects.get(tiny_text=tiny_text)
    goto_IP = request.META['REMOTE_ADDR']
    get_long.redirectIP = goto_IP
    get_long.save()
    print(f"redirecting to {get_long}")
    return HttpResponseRedirect(get_long.url_text)