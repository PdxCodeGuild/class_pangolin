from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, UserViewSet
# PostList, PostDetail, UserList, UserDetail

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
#     path('user/', UserList.as_view()),
#     path('user/<int:pk>/', UserDetail.as_view())
# ]

router = DefaultRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', PostViewSet, base_name='posts')

urlpatterns = router.urls