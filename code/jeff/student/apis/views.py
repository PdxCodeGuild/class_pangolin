from django.shortcuts import render
from rest_framework import generics, viewsets
from django.contrib.auth.models import User

from students.models import Student
from .serializers import StudentSerializer, UserSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
