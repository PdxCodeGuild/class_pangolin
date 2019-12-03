from django.urls import path
from . import views

app_name = 'list'
urlpatterns = [
    path('', views.index, name="index"),
    path('hidden_add/', views.hidden_add, name="hidden_add"),
    path('add/', views.add, name="add"),
    path('buy/<int:item_id>', views.buy, name="buy"),
    path('delete/<int:item_id>', views.delete, name="delete")
]