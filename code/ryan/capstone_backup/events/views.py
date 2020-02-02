from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django .views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from django.http import HttpResponseRedirect
from .models import Event
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'events/home.html')

class EventListView(ListView):
    model = Event
    template_name = 'events/locals.html'
    context_object_name = 'events'

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['band', 'body', 'venue', 'street_address', 'city', 'state', 'date', 'time', 'price', 'image', 'url']
    success_url = '/profile/'

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['band', 'body', 'venue', 'street_address', 'city', 'state', 'date', 'time', 'price']
    success_url = '/profile/'

@login_required
def add_event(request):
    return render(request, 'events/profile.html')

@login_required
def profile(request):
    return render(request, 'events/profile.html')

def locals(request):
    return render(request, 'events/locals.html')

