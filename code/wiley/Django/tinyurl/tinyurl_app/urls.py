from django.urls import path

from . import views



app_name = "tinyurl_app"
urlpatterns = [
    path('shorten/', views.shorten, name="shorten"),
    path('s/<str:tiny_text>/', views.index, name='index_with_short'),
    path('redirecting/<str:tiny_text>/', views.redirecting, name="redirecting"),
    path('', views.index, name='index'),

]