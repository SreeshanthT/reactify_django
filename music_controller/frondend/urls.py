from django.urls import path,include
from frondend.views import index

urlpatterns = [
    path('',index),
]