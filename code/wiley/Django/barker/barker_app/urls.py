from django.urls import path, reverse

from . import views

app_name = 'barker_app'

urlpatterns = [
    path('', views.BarkListView.as_view(), name='home'),
    path('bark/<int:pk>/', views.BarkDetailView.as_view(), name='detail'),
    path('bark/fresh_bark/', views.BarkCreateView.as_view(), name='fresh'),
    path('bark/<int:pk>/delete', views.BarkDeleteView.as_view(), name='delete'),
    path('bark/<int:pk>/likes/', views.like_post, name='likes'),
    path('bark/<int:pk>/dislike/', views.dislike_post, name='dislike'),
]