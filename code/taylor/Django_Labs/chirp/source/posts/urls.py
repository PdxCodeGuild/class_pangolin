from django.urls import path 
from .views import PostListView, PostCreateView, UserPostListView
from . import views
from users import views as user_views

urlpatterns = [
  path('', PostListView.as_view(), name='index'),
  path('users/', PostCreateView.as_view(), name='post-create'),
  path('users/<str:username>', UserPostListView.as_view(), name='user-post'),
]
