from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name = 'user_list'),
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('posts/<str:user>/', views.UserPostListView.as_view(), name = 'user_post_list')
]