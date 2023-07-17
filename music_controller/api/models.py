from django.db import models
import string
import random

def code_generator():
    length = 6
    
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k = length))
        #if the code has been never used, break the loop
        if Room.objects.filter(code= code).count() == 0:
            break
        
    return code
        

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default=code_generator, unique=True)
    host = models.CharField(max_length=50, unique=True) #only one unique host
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    current_song = models.CharField(max_length=50, blank=True)
    