from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created')