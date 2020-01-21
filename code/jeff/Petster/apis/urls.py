from django.contrib import admin
from django.urls import include, path

from .views import ListPet, DetailPet

urlpatterns = [
    path('<int:pk>/', DetailPet.as_view()),
    path('', ListPet.as_view()),
]
