from django.shortcuts import render
from rest_framework import generics, viewsets
from django.contrib.auth.models import User

from students.models import Student
from .serializer import StudentSerializer, UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
