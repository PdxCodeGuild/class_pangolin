from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('short_url/', views.index, name='short_index'),
    path('shorten/', views.shorten, name="shorten"),
    # path('', views.Shortener_appListView.as_view(), name='home'),
]
