from django.urls import path, include
from django.views.generic import TemplateView

from . import views
from .views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', StudentViewSet, basename='students')
urlpatterns = router.urls

app_name = 'students'
urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('v1/', include(router.urls))
]

# from django.urls import path


