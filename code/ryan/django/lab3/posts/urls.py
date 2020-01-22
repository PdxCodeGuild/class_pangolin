from django.urls import path
from .views import PostListView, PostCreateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='post-home'),
    path('login/', views.login, name="post-login"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
]
