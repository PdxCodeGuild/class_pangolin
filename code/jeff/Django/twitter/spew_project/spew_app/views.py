from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    return render(request, 'spew_app/index.html', {'title': 'Index'})


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'spew_app/home.html', context)


def about(request):
    return render(request, 'spew_app/about.html', {'title': 'About'})


def register(request):
    return render(request, 'spew_app/register.html', {'title': 'Register'})
