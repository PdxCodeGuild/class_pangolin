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
    print('abc')
    print(tiny_text)
    return render(request, 'tinyurl_app/index.html', context)

def shorten(request):
    print('hi')
    user_input = request.POST['user_url']
    shorten_call = ''.join(random.choice(string.ascii_letters) for i in range(8))
    var = LongUrl.objects.create(url_text = user_input, tiny_text=shorten_call)
    print(f"THIS IS A STRING WITH THE TINY URL {var.showtiny}")
    return HttpResponseRedirect(reverse('tinyurl_app:index_with_short', args=(var.tiny_text,)))

def redirecting(request, tiny_text):
    get_long = LongUrl.objects.get(tiny_text=tiny_text)
    print(get_long)
    return HttpResponseRedirect(get_long.url_text)