from django.urls import path
from . import views
app_name = 'short_url'
urlpatterns = [
    path('', views.submit_url, name='index' ),
    path('short/', views.short, name='short'),
    path('redirect/<str:short_code>/', views.redirect, name='redirect')
]

