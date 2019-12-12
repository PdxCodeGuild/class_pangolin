from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Twitter

class TweetListView(ListView):
    model = Twitter
    template_name = 'home_page.html'

class TweetDetailView(DetailView):
    model = Twitter
    template_name = 'post_detail.html'

class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Twitter
    template_name = 'post_new_post.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TweetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Twitter
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:home_page')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author