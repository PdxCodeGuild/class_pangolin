from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import GroceryItem
from django.http import HttpResponse

# Create your views here.

def index(request):
    items = GroceryItem.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'grocerylist_app/index.html', {'items':items})
    # return HttpResponse('<h1>Hello World Wide Web!</h1>')