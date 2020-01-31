from rest_framework import serializers

from events.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('band',
        'body',
        'venue',
        'street_address', 
        'city', 
        'state', 
        'date', 
        'time',
        'price',
        'date_created',
        'author'
        )