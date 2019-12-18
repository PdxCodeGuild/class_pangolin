from django.urls import path
from django.conf import settings
			
from . import views

app_name = "posts"
urlpatterns = [
    path('', views.BirdbrainListView.as_view(), name='home'),
    path('post/<int:pk>/', views.BirdbrainDetailView.as_view(), name='detail'),
    path('post/new/', views.BirdbrainCreateView.as_view(), name='new'),
    path('post/<int:pk>/edit', views.BirdbrainUpdateView.as_view(), name='edit'),
    path('post/<int:pk>/delete', views.BirdbrainDeleteView.as_view(), name='delete'),
    
]