from rest_framework import serializers
from .models import Organisers, Events

class OrganiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisers 
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events 
        fields = '__all__'