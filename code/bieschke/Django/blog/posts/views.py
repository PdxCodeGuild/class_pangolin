from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#Mixin is a class that adds functionality through inheritance

from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']  #make sure to implement the user association
    #fields = '__all__' find all fields associated 
    #with this model and create new fields
    #currently allows us to edit all fields for posting

    def form_valid(self, form):
        form.instance.author = self.request.user    #add this to the form
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']  #order matters here
    template_name = 'post_edit.html'

    def test_func(self):
        obj = self.get_object() #get the post
        return self.request.user == obj.author  #checks if the user making the 
                                                #request is the same as the author

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:home')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author  

        #return self.request.user.is_superuser     #will only let the admin delete a post
