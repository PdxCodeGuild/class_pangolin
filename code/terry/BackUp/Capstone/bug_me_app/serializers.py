from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Ticket, File

class TicketSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Ticket
        fields = ('id', 'title', 'body', 'created', 'closed', 'file')
        optional_fields = ['file',]

class UserSerializer(serializers.ModelSerializer):
    bug_me_app = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'bug_me_app')

class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ('id', 'title', 'body', 'created', 'closed', 'file')
        optional_fields = ['file',]