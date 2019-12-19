from django.urls import path, include
from . import views

app_name = 'url_shortener_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('makeshort/', views.shorten_url, name="shortenurl"),
    path('<str:short_id>/', views.redirect_original, name="redirectoriginal"),
]
