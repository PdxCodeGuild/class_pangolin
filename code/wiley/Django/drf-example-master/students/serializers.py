from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Student
        fields = ['first_name','last_name','cohort','favorite_topic','favorite_teacher','capstone']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']