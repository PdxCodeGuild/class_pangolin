from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import GroceryItem
from django.utils import timezone

def listView(request):
    incomplete_items = GroceryItem.objects.filter(is_completed=False).order_by('-date_created')
    complete_items = GroceryItem.objects.filter(is_completed=True).order_by('-date_created')
    try:
        error = request.GET['error']
    except:
        error = None
    context = {
        'incomplete_items': incomplete_items,
        'complete_items': complete_items,
        'error': error,
        }
    return render(request, 'list.html', context)

def addItem(request):
    new_item = GroceryItem(content = request.POST['content'])
    new_item.date_created = timezone.now()
    new_item.save()
    return HttpResponseRedirect(reverse('grocery_app:list'))
    

def deleteItem(request, item_id):
    if request.method == 'POST':
    item_to_delete = get_object_or_404(GroceryItem, id=item_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/grocery_app/')

def completeItem(request, item_id):
    if request.method == 'POST':   
        item_to_complete = GroceryItem.objects.get(id=item_id)
        item_to_complete.is_completed = True
        item_to_complete.date_completed = timezone.now()
        item_to_complete.save()
        return HttpResponseRedirect('/grocery_app/')
    else: raise Http404
# Create your views here.
