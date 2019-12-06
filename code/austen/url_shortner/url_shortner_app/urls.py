from django.urls import path

from . import views


app_name = 'url_shortner_app'
urlpatterns = [
    path('',views.index, name='index'),
    path('user_input/', views.user_input, name='user_input'),
    path('results/<str:short_url>/',views.results, name='results')
    # path('results/short_url',views.results, name='results')
   
]
