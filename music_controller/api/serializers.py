from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause',
                  'votes_to_skip', 'created_at')

class CreateRoomSerializer(serializers.ModelSerializer):
    #when create a new room, we don't need code, host and created_at, as they are automatically generated
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')
        
class UpdateRoomSerializer(serializers.ModelSerializer):
    #no validation is performaed during update operations
    code = serializers.CharField(validators=[])
    
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip', 'code')