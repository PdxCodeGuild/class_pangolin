from django.urls import path
from . import views

app_name = 'madlibapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:madlib_id>/', views.edit, name='edit'),
    path('play/<int:madlib_id>/', views.play, name='play'),
    path('view/<int:madlib_id>/', views.view, name='view'),
]
