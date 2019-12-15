from django.urls import path 
from . import views

urlpatterns = [
 
  path('registration/', views.user_registration, name='registration-home'),
  path('', views.users, name='users-home'),
]
