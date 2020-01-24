from django.shortcuts import render
from rest_framework import generics, viewsets
from django.contrib.auth.models import User

from .serializers import UserSerializer
# from rest_framework.viewsets import APIView
# from rest_framework.response import response
from rest_framework import status
from apis import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
