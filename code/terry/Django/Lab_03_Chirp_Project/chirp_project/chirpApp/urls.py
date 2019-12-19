from django.urls import path

from . import views

app_name = 'chirpApp'

urlpatterns = [
    path('', views.ChirpList.as_view(), name='index'),
    path('Chirp/<int:pk>/', views.ChirpDetail.as_view(), name='detail'),
    path('Chirp/create/', views.ChirpCreate.as_view(), name='create'),
    path('Chirp/<int:pk>/edit/', views.ChirpUpdate.as_view(), name='edit'),
    path('Chirp/<int:pk>/delete/', views.ChirpDelete.as_view(), name='delete'),
]