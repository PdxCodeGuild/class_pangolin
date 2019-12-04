from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem

# main page that is shown, it is saying order objects in newst first order and return to main page 
def index(request):

    context = {'latest_grocery_list': GroceryItem.objects.filter(is_completed= False).order_by('created_date'), 'finished_grocery_list': GroceryItem.objects.filter(is_completed=True).order_by('created_date')}

    return render(request, "grocery_app/index.html", context)

# to change null value to true and then update it to delete it from the database
def purchase(request, grocery_id):
    grocery = get_object_or_404(GroceryItem, pk=grocery_id)
    grocery.is_completed =True
    grocery.completed_date = timezone.now()
    grocery.save()

# #this if statement is making it so that if the top button gets clicked then go ahead and delete it from the list 
#     if grocery.is_completed == True:
#         grocery.delete()

    return HttpResponseRedirect(reverse('grocery_app:index'))

#adding a value to the data base, set the request.POST to a value and have the []= the name in your html.form
def add_stuff(request):
    input_answer = request.POST['stuff']
    GroceryItem.objects.create(text_discription= input_answer, created_date=timezone.now())
    return HttpResponseRedirect(reverse('grocery_app:index'))

def delete(request):
    finished = GroceryItem.objects.filter(is_completed=True)

    for items in finished:
        items.delete()

    return HttpResponseRedirect(reverse('grocery_app:index'))