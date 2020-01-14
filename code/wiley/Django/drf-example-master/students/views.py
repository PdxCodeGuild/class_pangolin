from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import StudentSerializer, GroupSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = StudentSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer