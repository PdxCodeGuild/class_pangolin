from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from books.models import Book

# Create your views here.
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer