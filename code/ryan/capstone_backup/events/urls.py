from django.urls import path
from .views import EventListView, EventCreateView
from . import views
urlpatterns = [
    path('locals/', EventListView.as_view(), name='locals'),
    path('event/new/', EventCreateView.as_view(), name='create'),
    path('profile/', views.profile, name='profile'),
    path('', views.home, name='events-home'),

]
