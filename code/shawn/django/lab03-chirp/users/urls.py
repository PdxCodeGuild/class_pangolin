from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    path('edit/<int:pk>/', views.EditProfileView.as_view(), name='profile_edit'),
    # path('follow/<int:profile_id>', views.FollowProfileView.as_view(), name='profile_follow'),
    path('follow/', views.follow, name='profile_follow'),
    path('unfollow/', views.unfollow, name='profile_unfollow'),
    path('<str:username>/', views.UserProfileView.as_view(), name='profile'),
]
