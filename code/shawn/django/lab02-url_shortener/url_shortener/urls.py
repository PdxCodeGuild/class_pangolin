from django.urls import path
from . import views

app_name = "url_shortener"
urlpatterns = [
    path('generate_code/', views.generate_code, name="generate_code"),
    path('go/<str:short_code>/', views.redirect_to_long_url, name="go"),
    path('pairs/', views.pairs, name="pairs"),
    path('contact/', views.contact, name="contact"),
    path('<str:generated_code>/', views.submit_url, name="submit_url_with_code"),
    path('', views.submit_url, name="submit_url"),
]
