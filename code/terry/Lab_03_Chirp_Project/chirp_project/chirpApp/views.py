from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Chirp

class ChirpList(ListView):
    model = Chirp
    template_name = 'index.html'

class ChirpDetail(DetailView):
    model = Chirp
    template_name = 'detail.html'

class ChirpCreate(CreateView):
    model = Chirp
    template_name = 'create.html'

class ChirpUpdate(UpdateView):
    model = Chirp
    template_name = 'edit.html'

class ChirpDelete(DeleteView):
    model = Chirp
    template_name = 'delete.html'