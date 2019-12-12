from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class BlogListView(ListView):
    model = Post                    # telling it to list the posts
    template_name = 'home.html'     # telling it which template to use

class BlogDetailView(DetailView):
    model = Post                    # look within this model.  this will be sent in automatically in the context as both 'post' and 'object'
    template_name = 'post_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    # the create view will automatically handle both GET and POST.
    # so you can post directly back to the same view and it'll render differently
    model = Post
    template_name = 'post_new.html'

    # instead of sending in all form elements, we're only going to send in title and body, 
    # and then manually send the author so that we can make the user non-editable 
    fields = ['title', 'body']       

    def form_valid(self, form):
        form.instance.author = self.request.user        # this will return a user object and add to form
        return super().form_valid(form)                 # insert this form into the form used by BlogCreateView

class BlogEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']          # this will be in order of how they are displayed on screen

    def test_func(self):
        # get the blogpost
        obj = self.get_object()
        # make sure logged in user (self.request.user) is the same as the author (obj.author)
        return self.request.user == obj.author

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('posts:home') # must gie DeleteView a URL to redirect to once successful

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author