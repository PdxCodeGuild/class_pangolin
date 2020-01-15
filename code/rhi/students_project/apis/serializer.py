from rest_framework import serializers
from django.contrib.auth.models import User

from students.models import Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'cohort', 'favorite_topic', 'favorite_teacher', 'capstone')