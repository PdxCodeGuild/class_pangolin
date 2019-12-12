from django.urls import path
from . import views

app_name='grocerylist_app'
urlpatterns = [
    path('', views.index, name='index'), 
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('addItem/', views.addItem, name='add_item'),
    path('deleteItem/<int:item_pk>/', views.deleteItem, name='delete_item'),
    path('completedItem/<int:item_pk>/', views.completedItem, name='completed_item'),
]
