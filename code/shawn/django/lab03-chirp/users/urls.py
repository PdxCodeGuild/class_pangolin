from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    path('edit/<int:pk>/', views.EditProfileView.as_view(), name='profile_edit'),
    path('follow/', views.FollowProfileView.as_view(), name='profile_follow'),
    path('unfollow/<int:pk>/', views.UnfollowProfileView.as_view(), name='profile_unfollow'),
    path('<str:username>/', views.UserProfileView.as_view(), name='profile'),
]
