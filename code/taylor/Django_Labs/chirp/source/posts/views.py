from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


# def index(request):
#   context = {
#     'posts': Post.objects.all()
#     }
#   return render(request, 'posts/index.html', context)

class PostListView(ListView):
  model = Post
  template_name = 'posts/index.html'
  context_object_name = 'posts'
  ordering = ['-date_posted']

class PostCreateView(CreateView):
  model = Post
  template_name = 'users/users.html'
  fields = ['title', 'content']
  success_url = '/'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)