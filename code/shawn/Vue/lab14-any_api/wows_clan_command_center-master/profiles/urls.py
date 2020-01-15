from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('stats', views.DetailPlayerView.as_view(), name='detail'),
]
