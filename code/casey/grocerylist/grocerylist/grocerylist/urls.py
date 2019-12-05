from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_item, name='add_entry'),
    path('complete/<int:pk>/', views.entry_completed, name='entry_completed'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('admin/', admin.site.urls),
]
