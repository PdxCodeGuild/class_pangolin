from django.urls import path, include
from django.contrib import admin
from . import views



app_name = 'grocery_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:GroceryItem_id>/', views.index, name='index'),
    path('add_item/', views.add_item, name="add_item"),
    path('purchased/<int:GroceryItem_id>/', views.purchased, name="purchased"),
    path('delete/', views.delete, name="delete"),
]
