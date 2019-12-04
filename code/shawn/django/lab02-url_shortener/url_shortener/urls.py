from django.urls import path
from . import views

app_name = "url_shortener"
urlpatterns = [
    path('', views.submit_url, name="submit_url"),
    path('generate_code/', views.generate_code, name="generate_code")
]
