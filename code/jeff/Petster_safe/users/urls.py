from django.urls import path
# from . import views
from .views import profile, register, home, about
from users import views as user_views

app_name = 'users'
urlpatterns = [
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('about/', about, name='about'),
    # path('', profile, name='pets-profile'),
]
