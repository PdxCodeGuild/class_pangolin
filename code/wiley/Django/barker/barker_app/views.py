from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404 
from django.http import  Http404, HttpResponseRedirect


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
    

class BarkDeleteView(UserPassesTestMixin, DeleteView):
    model = Bark
    template_name = 'delete.html'
    success_url = reverse_lazy('barker_app:home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



@login_required
def like_post(request, pk):
    if request.method=="POST":
        bark = get_object_or_404(Bark, pk=pk)
        bark.dislike.remove(request.user)
        bark.likes.add(request.user)
        bark.save()
        return HttpResponseRedirect(reverse('barker_app:home'))

    else:
        raise Http404()        

@login_required
def dislike_post(request, pk):
    if request.method=="POST":
        bark = get_object_or_404(Bark, pk=pk)
        bark.likes.remove(request.user)
        bark.dislike.add(request.user)
        bark.save()
        return HttpResponseRedirect(reverse('barker_app:home'))

    else:
        raise Http404()  