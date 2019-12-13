from . import views
from django.conf.urls import url
from glist import views
from django.urls import path

app_name = 'glist'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_item, name='add_item'),
    path('complete/<int:pk>/', views.mark_complete, name='mark_complete'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
