from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect
from .models import GroceryItem 
from django.utils import timezone
from django.urls import reverse
# Create your views here.

def index(request):
    all_items = GroceryItem.objects.order_by('-date_created')
    return render(request, 'grocery_list.html', 
    {'full_list': all_items})

def add_item(request):
    if request.method == 'POST':
        new_item = GroceryItem.objects.create(content = request.POST['content'], date_created=timezone.now())
        return HttpResponseRedirect(reverse('grocery_app:index'))
    else:
        raise Http404    

def delete_item(request, pk):
    if request.method == 'POST':
        delete_item = get_object_or_404(GroceryItem, pk=pk)
        delete_item.delete()
        return HttpResponseRedirect(reverse('grocery_app:index'))
    else:
        raise Http404

def complete_item(request, pk):
    if request.method == 'POST':
        complete = get_object_or_404(GroceryItem, pk=pk)
        complete.date_completed = timezone.now()
        complete.completed = True
        complete.save()
        return HttpResponseRedirect(reverse('grocery_app:index'))
    else:
        raise Http404



