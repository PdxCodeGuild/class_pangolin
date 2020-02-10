from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.views.generic import ListView, CreateView
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'posts/home.html', context)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']
    success_url = '/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


def login(request):
    return render(request, 'posts/login.html')
