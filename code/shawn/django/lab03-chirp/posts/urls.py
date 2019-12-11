from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.ChirpHomeView.as_view(), name='home')
]
