from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Chirp, Comment, Reaction


class ChirpHomeView(ListView):
    model = Chirp
    template_name = 'home.html'

class FeedView(ListView):
    model = Chirp
    template_name = 'home_filtered.html'

class ChirpCreateView(LoginRequiredMixin, CreateView):
    model = Chirp
    template_name = 'create.html'

    fields = ['text', 'picture']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ChirpEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Chirp
    template_name = 'edit.html'

    fields = ['text', 'picture']

    def test_func(self):
        # get the chirp
        obj = self.get_object()
        # make sure logged in user (self.request.user) is the same as the author (obj.author)
        return self.request.user == obj.author

class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chirp
    template_name = "delete.html"
    success_url = reverse_lazy('posts:home') # must give DeleteView a URL to redirect to once successful

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

class ChirpDetailView(DetailView):
    model = Chirp
    template_name = 'chirp.html'

    