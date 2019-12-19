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

class ChirpCreate(LoginRequiredMixin, CreateView):
    model = Chirp
    template_name = 'create.html'
    fields = ['body_text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ChirpUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Chirp
    template_name = 'edit.html'
    fields = ['body_text']

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author


class ChirpDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chirp
    template_name = 'delete.html'
    success_url = reverse_lazy('chirpApp:index')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

