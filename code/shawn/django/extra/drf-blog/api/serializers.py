from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'last_login')

class PostSerializer(serializers.ModelSerializer):

    # an additional field that's not in the model, referencing an item in the User serializer in this case
    author_name = UserSerializer(read_only=True, source="author")

    class Meta:
        model = Post
        fields = ('id', 'author', 'author_name', 'title', 'body', 'created')
