from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='spew_app-index'),
    path('', views.home, name='spew_app-home'),
    path('about/', views.about, name='spew_app-about'),
]
