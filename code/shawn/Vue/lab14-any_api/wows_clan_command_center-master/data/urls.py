from django.urls import path
from . import views

app_name = 'data'
urlpatterns = [
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('update_user_clan/<str:realm>/', views.update_user_clan, name="update_user_clan"),
    path('update_game_data/<str:realm>/', views.update_game_data, name='update_game_data'),
]
