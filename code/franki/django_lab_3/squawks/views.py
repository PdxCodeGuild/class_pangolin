from django.shortcuts import render
from .models import Squawk
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class SquawkFeedView(ListView):
    model = Squawk
    template_name = 'home.html'

class SquawkDetailView(DetailView):
    model = Squawk
    template_name = 'home.html'

class SquawkCreateView(LoginRequiredMixin, CreateView):
    model = Squawk
    template_name = 'squawk_new.html'
    fields = ['body']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class SquawkEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Squawk
    fields = ['title', 'body']
    template_name = 'squawk_edit.html'
    
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

class SquawkDeleteView(DeleteView):
    model = Squawk
    template_name = 'squawk_delete.html'
    success_url = reverse_lazy('squawks:home')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author