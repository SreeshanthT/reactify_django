from django.db import models

import string
import random
# Create your models here.

def generate_unique_code(length=6):
    while True:
        code = "".join(random.choices(string.ascii_uppercase, k=length))
        if not Room.objects.filter(code = code).exists():
            break

    return code


class Room(models.Model):
    code = models.CharField(max_length=8,unique=True,default="")
    host = models.CharField(max_length=50,unique=True)
    guest_can_pause = models.BooleanField(default=False)
    votes_to_skip = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
