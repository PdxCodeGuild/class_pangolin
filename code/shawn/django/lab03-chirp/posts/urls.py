from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.ChirpHomeView.as_view(), name='home'),
    path('feed/', views.FeedView.as_view(), name='home_filtered'),
    path('create/', views.ChirpCreateView.as_view(), name='create'),
    path('view/<int:pk>', views.ChirpDetailView.as_view(), name='view'),
    path('delete/<int:pk>', views.ChirpDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', views.ChirpEditView.as_view(), name='edit'),
    path('comment/<int:pk>/', views.CommentAddView.as_view(), name='add_comment'),
    path('comment_edit/<int:pk>/', views.EditCommentView.as_view(), name='edit_comment'),
    path('comment_delete/<int:pk>/', views.DeleteCommentView.as_view(), name='delete_comment'),
    path('like/', views.like, name='like'),
    path('dislike/', views.dislike, name='dislike'),
]
