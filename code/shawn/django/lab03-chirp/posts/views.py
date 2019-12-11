from django.shortcuts import render
from django.views.generic import ListView
from .models import Chirp, Comment, Reaction

class ChirpHomeView(ListView):
    model = Chirp
    template_name = 'home.html'
