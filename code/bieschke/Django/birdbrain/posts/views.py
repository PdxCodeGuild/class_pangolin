from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#Mixin is a class that adds functionality through inheritance

from .models import Post

class BirdbrainListView(ListView):
    model = Post
    template_name = 'posts/home.html'

class BirdbrainDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

class BirdbrainCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/new.html'
    fields = ['brain', 'peekchure']
    success_url = reverse_lazy('posts:home')    #url tag in the view instead of the template

    def form_valid(self, form):
        form.instance.author = self.request.user    #add this to the form
        return super().form_valid(form)

class BirdbrainUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['brain', 'peekchure']
    template_name = 'posts/edit.html'
    success_url = reverse_lazy('posts:home')

    def test_func(self):
        obj = self.get_object() #get the post
        return self.request.user == obj.author  #checks if the user making the 
                                                #request is the same as the author

class BirdbrainDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:home')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author
