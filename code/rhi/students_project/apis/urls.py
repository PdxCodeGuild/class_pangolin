from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet, UserViewSet

# urlpatterns = [
#     path('', StudentAPIView.as_view()),
# ]

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('students', StudentViewSet, basename='students')

urlpatterns = router.urls