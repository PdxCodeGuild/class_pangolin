from django.urls import path 
from .views import PostListView, PostCreateView
from . import views
from users import views as user_views

urlpatterns = [
  
  path('', PostListView.as_view(), name='index'),
  path('users/', PostCreateView.as_view(), name='post-create'),
 
]
