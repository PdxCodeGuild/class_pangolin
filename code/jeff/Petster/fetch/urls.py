from django.urls import path
from . import views

app_name = 'fetch'
urlpatterns = [
    path('', views.home, name='fetch-home'),
    path('about/', views.about, name='fetch-about'),


]
