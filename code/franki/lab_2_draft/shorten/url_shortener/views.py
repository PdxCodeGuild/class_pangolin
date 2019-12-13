from django.shortcuts import render
import random
import string
from django.http import HttpResponseRedirect

def homeView(request):
    # try:
    #     error = request.GET['error']
    # except:
    #     error = None
    # context = {
    #     'error': error,
    #     }
    return render(request, 'home.html', context)

def submitUrl(request):
    code = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])
    return HttpResponseRedirect

def redirectUser(request, code):
    url = Abbreviation.objects.get(code) 
    return HttpResponseRedirect(url)
