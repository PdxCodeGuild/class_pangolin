from rest_framework import serializers
from users import models 

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'username',
            'email',
            'company',
            'date_joined',
        )
        model = models.CustomUser 