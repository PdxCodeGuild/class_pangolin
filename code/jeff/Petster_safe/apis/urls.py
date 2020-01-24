from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

# Register different routers for the vewsets
router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls
