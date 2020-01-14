from django.urls import path
from .views import BookListView

appname = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name="list")
]