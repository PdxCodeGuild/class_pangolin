from django.urls import path
from . import views

app_name = 'grocery_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_item, name='add'),
    path('delete/<int:pk>/', views.delete_item, name='delete'),
    path('complete/<int:pk>/', views.complete_item, name='complete')
]
