from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import UrlPair, Hit

import random
import string
from . import secrets
import requests

# View for submitting URLs to shorten
def submit_url(request, generated_code=''):
    context = {"short_url": generated_code}
    return render(request, 'url_shortener/submit_url.html', context)

# A view (that shouldn't render anything for user) for generating shortened code
def generate_code(request):

    # try to get url
    try:
        get_long_url = request.POST['long-url']
    except:
        return render(request, 'url_shortener/submit_url.html', {'error_message': "Couldn't get URL"})

    # generate random 5 character code
    generated_code = ''
    possible_characters = string.ascii_letters + '1234567890'
    for i in range(5):
        generated_code += random.choice(possible_characters)

    # store long_url and code in db
    UrlPair.objects.create(code=generated_code, long_url=get_long_url)

    # redirect back to submit page
    # return HttpResponseRedirect(reverse('url_shortener:submit_url'))            ### how to get this redirect to send in args for the generated code?
    return HttpResponseRedirect(reverse('url_shortener:submit_url_with_code', args=(generated_code,)))

# A view to send user to long url
def redirect_to_long_url(request, short_code):

    # get long URL from db
    pair = UrlPair.objects.get(code=short_code)

    # try to get metadata information from user
    ip = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    
    # lookup location of ip using ipstack api
    ip_lookup_url = f"http://api.ipstack.com/{ip}?access_key={secrets.api_key}"
    response = requests.get(ip_lookup_url).json()
    location_string = f"{response['city']}, {response['country_name']}"
    if location_string == "None, None":
        location_string = "Location not found."

    # create new Hit object
    Hit.objects.create(ip_address=ip, host_name=user_agent, location=location_string, urlpair_key=pair)

    # redirect to long URL
    return HttpResponseRedirect(pair.long_url)

# a view for the pairs page
def pairs(request):
    context = {'pair_list': UrlPair.objects.all()}
    print("rendering pairs")
    return render(request, 'url_shortener/pairs.html', context)

# a view for the contacts page
def contact(request):
    context = {}
    print("rendering contacts")
    return render(request, 'url_shortener/contact.html', context)