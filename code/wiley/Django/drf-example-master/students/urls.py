from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from . import views

# router = routers.DefaultRouter()#test
# router.register(r'users', views.StudentViewSet)#test
# router.register(r'groups', views.GroupViewSet)#test

app_name = 'students'
urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),

]