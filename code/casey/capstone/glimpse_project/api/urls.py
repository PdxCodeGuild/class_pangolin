from django.urls import path

from .views import ListUsers, DetailUsers

urlpatterns = [
    path('', ListUsers.as_view()),
    path('<int:pk>/', DetailUsers.as_view()),
]