from django.urls import path,include
from music_api.views import RoomView


urlpatterns = [
    path('',RoomView.as_view(),name='room-create'),
]