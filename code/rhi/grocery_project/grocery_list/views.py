from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem
from .forms import AddForm


# Create your views here.
def index(request):
    incomplete_items = GroceryItem.objects.filter(is_completed=False).order_by('-date_created')
    complete_items = GroceryItem.objects.filter(is_completed=True).order_by('-date_completed')
    form = AddForm()
    try:
        error = request.GET['error']
    except:
        error = None
    context = {
        'incomplete_items': incomplete_items,
        'complete_items': complete_items,
        'form': form,
        'error': error,
        } 
    return render(request, 'grocery_list/index.html', context)


def add_item(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            GroceryItem.objects.create(name=form.cleaned_data['name'], date_created=timezone.now())
            return HttpResponseRedirect(reverse("grocery_list:index"))
    else:
        raise Http404()

def mark_complete(request,pk):
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, pk=pk)
        item.is_completed = True
        item.date_completed = timezone.now()
        item.save()
        return HttpResponseRedirect(reverse('grocery_list:index'))
    else: 
        raise Http404


def delete(request, pk):
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, pk=pk)
        item.delete()
        return HttpResponseRedirect(reverse('grocery_list:index'))
    else:
        raise Http404
