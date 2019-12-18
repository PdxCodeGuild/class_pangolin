from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.contrib.auth.models import User

class PostListView(ListView):
  model = Post
  template_name = 'posts/index.html'
  context_object_name = 'posts'
  ordering = ['-date_posted']
  paginate_by = 6

class UserPostListView(ListView):
  model = Post
  template_name = 'posts/user_posts.html'
  context_object_name = 'posts'
  paginate_by = 6

  def get_queryset(self):
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('-date_posted')

class PostCreateView(CreateView):
  model = Post
  template_name = 'users/users.html'
  fields = ['title', 'content']
  success_url = '/'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)