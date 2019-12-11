from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic


from .models import GroceryItem
from django.http import HttpResponse


def index(request):
    items = GroceryItem.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'grocerylist_app/index.html', {'items':items})
    # return HttpResponse('<h1>Hello World Wide Web!</h1>')

def addItem(request):
    new_item = GroceryItem(title = request.POST['title'], description = request.POST['description'])
    new_item.save()
    return HttpResponseRedirect(reverse('grocerylist_app:index'))

def deleteItem(request, item_pk):
    delete_item = get_object_or_404(GroceryItem, pk=item_pk)
    delete_item.delete()
    return HttpResponseRedirect(reverse('grocerylist_app:index'))

def completedItem(request, item_pk):
    completed_item = get_object_or_404(GroceryItem, pk=item_pk) #(title = request.POST['title'], description = request.POST['description'])
    completed_item.completed = True
    completed_item.completed_date = timezone.now()
    completed_item.save()
    return HttpResponseRedirect(reverse('grocerylist_app:index'))

def item_detail(request, pk):
    items = get_object_or_404(GroceryItem, pk=pk)
    return render(request, 'grocerylist_app/index.html', {'items': items})