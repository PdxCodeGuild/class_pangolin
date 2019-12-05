from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import GroceryEntry
from .forms import CreateForm


def index(request):
    completed_entries = GroceryEntry.objects.filter(is_completed=True).order_by('date_completed')
    incomplete_entries = GroceryEntry.objects.filter(is_completed=False).order_by('date_created')
    form = CreateForm()
    try:
        error = request.GET['error']
    except:
        error = None
    context = {
        'completed_entries': completed_entries,
        'incomplete_entries': incomplete_entries,
        'form': form,
        'error': error,
    }
    return render(request, 'grocerylist/index.html', context)

def add_entry(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            GroceryEntry.objects.create(name=form.cleaned_data['name'], date_created=timezone.now())
            return HttpResponseRedirect(reverse('grocery:index'))
        else:
            return HttpResponseRedirect(f'{reverse("grocery:index")}?error=Please submit a grocery list entry')

        else:
            raise Http404()
    
    def entry_completed(request, pk):
        if request.method == 'POST':
            entry = get_object_or_404(GroceryEntry, pk=pk)
            entry.is_completed = True
            entry.date_completed = timezone.now()
            entry.save()
            return HttpResponseRedirect(reverse('grocerylist:index'))
        else:
            raise Http404()

    def delete(request, pk):
        if request.method == 'POST':
            entry = get_object_or_404(GroceryEntry, pk=pk)
            entry.delete()
            return HttpResponseRedirect(reverse(grocerylist:index))
        else:
            raise Http404()
