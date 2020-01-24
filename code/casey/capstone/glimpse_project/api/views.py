from rest_framework import generics

from api import models
from .serializers import UsersSerializer
from users.models import CustomUser

class ListUsers(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer


class DetailUsers(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer