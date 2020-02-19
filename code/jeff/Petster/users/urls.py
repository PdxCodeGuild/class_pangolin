from django.urls import path
from . import views
from .views import profile, register
from users import views as user_views

app_name = 'fetch'
urlpatterns = [
    # path('', views.index, name='spew_app-index'),
    path('home/', views.home, name='fetch-home'),
    path('about/', views.about, name='fetch-about'),
    path('', profile, name='fetch-profile'),
]
