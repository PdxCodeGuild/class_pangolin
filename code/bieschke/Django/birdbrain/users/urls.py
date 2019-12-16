from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.UserSignUp.as_view(), name='profile_create'),
    path('<str:username>/', views.UserProfileView.as_view(), name='profile'),
]