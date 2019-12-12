from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.ChirpHomeView.as_view(), name='home'),
    path('create/', views.ChirpCreateView.as_view(), name='create'),
    path('delete/<int:pk>', views.ChirpDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', views.ChirpEditView.as_view(), name='edit'),
]
