from django.urls import path
from . import views

app_name='shortener_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('short_url/', views.index, name='short_index'),
    path('shorten/', views.shorten, name="shorten"),
]
