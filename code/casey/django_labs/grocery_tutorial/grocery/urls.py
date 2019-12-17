from django.urls import path
from . import views

app_name = 'grocery'
urlspatterns = [
    path('', views.index, name='index'),
]