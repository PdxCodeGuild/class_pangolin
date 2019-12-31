from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import GroceryItem
from django.utils import timezone
import pytz

def groceryappView(request):
    # all_grocery_items = GroceryItem.objects.all()
    # return render(request, 'groceryapp.html', {'all_items': all_grocery_items})
    incomplete_items = GroceryItem.objects.filter(is_completed=False).order_by('-date_created')
    completed_items = GroceryItem.objects.filter(is_completed=True).order_by('-date_created')
    try:
        error = request.GET['error']
    except:
        error = None
    context = {
        'incomplete_items': incomplete_items,
        'completed_items': completed_items,
        'error': error,
        }
    return render(request, 'groceryapp/groceryapp.html', context)

def addGrocery(request):
    new_item = GroceryItem(content = request.POST['content'])
    new_item.date_created = timezone.now()
    new_item.save()
    return HttpResponseRedirect('/groceryapp/')

def deleteGrocery(request, grocery_id):
    item_to_delete = GroceryItem.objects.get(id=grocery_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/groceryapp/')

def completeGrocery(request, grocery_id):
    item_to_complete = GroceryItem.objects.get(id=grocery_id)
    item_to_complete.is_completed = True
    item_to_complete.date_completed = timezone.now()
    item_to_complete.save()
    return HttpResponseRedirect('/groceryapp/')
