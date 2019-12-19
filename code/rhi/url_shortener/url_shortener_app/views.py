import random
import string
import json
from url_shortener_app.models import Urls
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse, HttpRequest
from django.conf import settings
from django.template.context_processors import csrf

# Create your views here.


def index(request):
    content = {}
    content.update(csrf(request))
    return render(request, 'url_shortener_app/index.html', content)

def redirect_original(request, short_id):
    url = get_object_or_404(Urls, short_id=short_id)
    url.count += 1
    url.ip_orig = request.META['REMOTE_ADDR']
    url.save()
    return HttpResponseRedirect(url.httpurl)

def shorten_url(request):
    url = request.POST.get("url", '')
    if not (url == ''):
        short_id = get_short_code()
        b = Urls(httpurl=url, short_id=short_id)
        b.save()

        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + short_id
        return HttpResponse(json.dumps(response_data),  content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")

def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.ascii_lowercase + string.digits
    #if the randomly generated short_id is used then generate next
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = Urls.objects.get(pk=short_id)
        except:
            return short_id
