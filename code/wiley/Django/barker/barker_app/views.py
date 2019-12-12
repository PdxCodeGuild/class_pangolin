from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bark

# Create your views here.
class BarkListView(ListView):
    model = Bark
    template_name = 'home.html'

class BarkDetailView(DetailView):
    model = Bark
    template_name = 'bark_detail.html'

class BarkCreateView(LoginRequiredMixin, CreateView):
    model = Bark
    template_name = "fresh_bark.html"
    fields = ['body']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class BarkDeleteView(DeleteView):
    model = Bark
    template_name = 'delete.html'
    success_url = reverse_lazy('barker_app:home')

    def test_func(self):
        obj = self.get_object()
        return self.request == obj.author


