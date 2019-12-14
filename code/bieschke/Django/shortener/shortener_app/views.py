from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Links

def redirect_view(request):
    return HttpResponse("Hello!")


def index(request):
    links = Links.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'shortener_app/index.html', {'links':links})
    # return HttpResponse('<h1>Hello World Wide Web!</h1>')

def shorten(request):
    shorten_link = models.Links.shorten.link
    return HttpResponseRedirect(reverse('shorten_app:index'))


def redirect(request):
    lengthen_link = models.Links.lengthen.link
    return HttpResponseRedirect(reverse('shorten_app:index'))

'''
from django.shortcuts import redirect, get_object_or_404

from shortlinks.models import Links
from shortlinks.utls import update_request_count_task

def link(request, id):
    db_id = Links.decode_id(id)
    link_db = get_object_or_404(Links, id=db_id, active=True, status=True)
    update_request_count_task.(db_id)
    return redirect(link_db.link)
'''