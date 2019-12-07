from django.urls import path
from . import views

app_name = 'madlibapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:madlib_id>/', views.edit, name='edit'),
    path('hidden_edit/<int:madlib_id>/', views.hidden_edit, name='hidden_edit'),
    path('play/<int:madlib_id>/', views.play, name='play'),
    path('view/<int:madlib_id>/', views.view, name='view'),
    path('delete/<int:madlib_id>/', views.hidden_delete, name='hidden_delete')
]
