from rest_framework import generics

from students.models import Student
from .serializers import StudentSerializer
# Create your views here.

class StudentAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
