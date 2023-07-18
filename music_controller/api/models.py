from django.db import models
import string
import random #for generating unique code to each user

def code_generator():
    length = 6
    
    while True:
        #Joins random letters together to form the code
        code = ''.join(random.choices(string.ascii_uppercase, k = length))
        #check if the generated code already exists in the room model
        if Room.objects.filter(code= code).count() == 0:
            break
        
    return code
        

# Create the room model that contains code, host, guest-can-vote boolean, votes-to-skip, create-time and current song
class Room(models.Model):
    code = models.CharField(max_length=8, default=code_generator, unique=True)
    host = models.CharField(max_length=50, unique=True) #only one unique host
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    current_song = models.CharField(max_length=50, blank=True)
    