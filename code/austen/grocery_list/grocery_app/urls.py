from django.urls import path

from . import views

app_name = 'grocery_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('purchase/<int:grocery_id>', views.purchase, name="purchase"),
    path('add_stuff/', views.add_stuff, name='add_stuff'),
    path('delete/', views.delete, name="delete"),
]