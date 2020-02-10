from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from .models import GroceryItem



# Create your views here.
# class IndexView(generic.ListView):
#     template_name = 'grocery_list.html'
#     context_object_name = 'items'

#     def get_queryset(self):
#         return GroceryItem.objects.order_by('-date_created')
def index(request):
    items = GroceryItem.objects.order_by('-date_created')
    context = {
       'items': items,
    }
    return render(request, 'grocery_list/index.html', context)

def item(request, GroceryItem_id):
    grocery_item = get_object_or_404(GroceryItem,pk=GroceryItem_id)

def add_item(request):
    item_name = request.POST["add_item"]
    if item_name == "":
        item_name = "You forgot something"
    GroceryItem.objects.create(text_description=item_name, date_created=timezone.now())
    return HttpResponseRedirect(reverse('grocery_list:index'))

def purchased(request, GroceryItem_id):
    grocery_item = get_object_or_404(GroceryItem, pk=GroceryItem_id)
    
    if grocery_item.completed == False:
        grocery_item.completed = True
        grocery_item.date_completed = timezone.now()
    elif grocery_item.completed == True:
        grocery_item.completed = False
    grocery_item.save()

    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete(request):
    completed_items = GroceryItem.objects.filter(completed=True)
      
    for completed_item in completed_items:
        completed_item.delete()  
    return HttpResponseRedirect(reverse('grocery_list:index'))
    

    
