from django.urls import path
from .views import (EventListView, EventCreateView, EventUpdateView, EventDeleteView)
from . import views
urlpatterns = [
    path('locals/', EventListView.as_view(), name='locals'),
    path('event/new/', EventCreateView.as_view(), name='create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='delete'),
    path('profile/', views.profile, name='profile'),
    path('', views.home, name='events-home'),

]
