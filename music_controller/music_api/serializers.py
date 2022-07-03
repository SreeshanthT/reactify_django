from dataclasses import field
import imp
from rest_framework import serializers
from music_api.models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'