from django.shortcuts import render
from rest_framework import generics 

from music_api.models import Room
from music_api.serializers import RoomSerializer


# Create your views here.

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer