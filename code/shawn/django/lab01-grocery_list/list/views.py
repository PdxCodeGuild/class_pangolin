from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import GroceryItem

# home page/list view
def index(request):
    context = {'incomplete_list': GroceryItem.objects.filter(is_completed=False),
               'complete_list': GroceryItem.objects.filter(is_completed=True)
               }
    return render(request, "list/index.html", context)

# add item view
def add(request):
    context = {}
    return render(request, "list/add.html", context)

# buy item view
def hidden_add(request):

    # try to get description from form
    try:
        input_description = request.POST['description']
    # if unable to find description, return to index 
    except KeyError:
        return HttpResponseRedirect(reverse("list:index"))

    # create new item on list using input description
    GroceryItem.objects.create(description_text=input_description, created_date=timezone.now(), completed_date=timezone.now(), is_completed=False)

    # redirect to home
    return HttpResponseRedirect(reverse('list:index'))

# buy item view
def buy(request, item_id):
    item = get_object_or_404(GroceryItem, pk=item_id)
    item.is_completed = True
    item.completed_date = timezone.now()
    item.save()

    return HttpResponseRedirect(reverse('list:index'))

# delete item view
def delete(request, item_id):
    item = get_object_or_404(GroceryItem, pk=item_id)
    item.delete()

    return HttpResponseRedirect(reverse('list:index'))


