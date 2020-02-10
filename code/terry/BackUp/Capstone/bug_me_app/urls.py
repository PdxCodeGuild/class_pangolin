from django.conf.urls import url, include
from django.urls import path
from bug_me_app import views
from .views import *

app_name = 'bug_me_app'

urlpatterns = [
    
    path('ticket/', views.TicketList.as_view()),
    path('ticket/<int:pk>/', views.TicketDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    # path('', views.api_root),
    path('logout', views.logout_request, name='logout'),
    path('login', views.login_request, name='login'),
    path('', views.index, name='index'),
    url(r'^upload/$', FileUploadView.as_view(), name='file-upload'),
]
