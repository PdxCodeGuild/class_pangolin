from django.shortcuts import render

from .models import GroceryItem

def index(request):
    context = {}
    return render(request, 'gorcery/index.html', context)