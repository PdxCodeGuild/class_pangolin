from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet, UserViewSet

router = DefaultRouter()
router.register('students', StudentViewSet, basename='students')
router.register('users', UserViewSet, basename='users')
urlpatterns = router.urls
