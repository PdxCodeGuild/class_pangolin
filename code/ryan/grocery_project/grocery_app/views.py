from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import GroceryItem
from django.utils import timezone
# Create your views here.

def index(request):
    all_items = GroceryItem.objects.all()
    return render(request, 'grocery_list.html', 
    {'full_list': all_items})

def add_item(request):
    new_item = GroceryItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/grocery_app/')

def delete_item(request, pk):
    delete_item = GroceryItem.objects.get(pk=pk)
    delete_item.delete()
    return HttpResponseRedirect('/grocery_app/')