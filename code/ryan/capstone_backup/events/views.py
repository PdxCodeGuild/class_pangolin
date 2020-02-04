from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django .views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponseRedirect
from .models import Event
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'events/home.html')

@login_required
def profile(request):
    user = request.user
    events = Event.objects.filter(author=request.user).order_by('-date_created')
    return render(request, 'events/profile.html', {'events':events,'user': user})

class EventListView(ListView):
    model = Event
    template_name = 'events/locals.html'
    context_object_name = 'events'

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['band', 'body', 'venue', 'street_address', 'city', 'state', 'date', 'time', 'price', 'image', 'url']
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Event
    template_name = 'events/event_update.html'
    fields = ['band', 'body', 'venue', 'street_address', 'city', 'state', 'date', 'time', 'price', 'image', 'url']
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    model = Event
    success_url = '/profile/'
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

def locals(request):
    return render(request, 'events/locals.html')



