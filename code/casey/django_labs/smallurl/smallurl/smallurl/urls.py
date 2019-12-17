from django.contrib import admin
from django.urls import path
from smallurlapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Make, name="Make new")
]
