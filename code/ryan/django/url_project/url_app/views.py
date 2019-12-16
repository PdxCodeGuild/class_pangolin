from django.shortcuts import get_object_or_404, render
from .models import UrlShortener
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
import string
import random
# Create your views here.

def submit_url(request):
    full_list = UrlShortener.objects.all()
    return render(request, 'index.html', {'full_list': full_list})

def short(request):
    if request.method == 'POST':
        full = request.POST['long']
        short_code = ""
        for i in range(6):
            short_code += random.choice(string.ascii_letters + string.digits)
        UrlShortener.objects.create(long_url = full, short=short_code)
        return HttpResponseRedirect(reverse('short_url:index'))
    else:
        raise Http404

def redirect(request, short_code):
    item = UrlShortener.objects.get(short = short_code)
    return HttpResponseRedirect(item.long_url)
    

    
