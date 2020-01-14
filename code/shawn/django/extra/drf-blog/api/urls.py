from django.urls import path


# for generics: 
# from .views import PostList, PostDetail, UserList, UserDetail
# appname = "api"
# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
#     path('', PostList.as_view(), name='post_list'),
#     path('user/', UserList.as_view(), name='user_list'),
#     path('user/<int:pk>/', UserDetail.as_view(), name='user_detail'),
# ]

# for viewsets
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls