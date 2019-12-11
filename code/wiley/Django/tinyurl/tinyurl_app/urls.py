from django.urls import path

from . import views



app_name = "tinyurl_app"
urlpatterns = [
    path('tu/<str:tiny_text>/', views.index, name='index_with_short'),
    path('shorten/', views.shorten, name="shorten"),
    path('<str:tiny_text>/', views.redirecting, name="redirecting"),
    path('', views.index, name='index'),

]