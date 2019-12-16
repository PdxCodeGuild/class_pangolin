from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post


class ChirpListView(ListView):
    model = Post
    template_name = 'posts/home.html'

class ChirpDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

class ChirpCreateView(CreateView):
    model = Post
    template_name = 'posts/new.html'
    fields = ['title', 'body']