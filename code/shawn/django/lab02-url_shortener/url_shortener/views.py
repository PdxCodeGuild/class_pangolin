from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import UrlPair

import random
import string

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
    return HttpResponseRedirect(reverse('url_shortener:submit_url'))            ### how to get this redirect to send in args for the generated code?