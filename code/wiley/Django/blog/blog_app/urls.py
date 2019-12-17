from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='detail')
]