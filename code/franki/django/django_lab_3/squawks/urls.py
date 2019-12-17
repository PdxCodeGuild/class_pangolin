from django.urls import path
from . import views
app_name = 'squawks'

urlpatterns = [
    path('', views.SquawkFeedView.as_view(), name='home'),
    path('squawk/<int:pk>/', views.SquawkDetailView.as_view(), name='detail'),
    path('squawk/new/', views.SquawkCreateView.as_view(), name='new'), 
    path('squawk/<int:pk>/edit/', views.SquawkEditView.as_view(), name='edit'), 
]