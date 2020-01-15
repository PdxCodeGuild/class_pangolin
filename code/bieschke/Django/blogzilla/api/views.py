from rest_framework import generics, viewsets
from django.contrib.auth.models import User

from posts.models import Post
from .serializers import PostSerializer, UserSerializer

# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class UserList(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewset.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer