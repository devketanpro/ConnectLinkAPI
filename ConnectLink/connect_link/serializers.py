from rest_framework import serializers
from connect_link.models import Interest
from user_app.models import User

class InterestSerializer(serializers.ModelSerializer):
    requested_user = serializers.SerializerMethodField()
    
    class Meta:
        model = Interest
        fields = ['id', 'sender', 'receiver', 'status', 'message', 'requested_user']
        read_only_fields = ['sender', 'status', 'timestamp']

    def validate(self, data):
        receiver = data.get('receiver')
        if receiver == self.context['request'].user:
            raise serializers.ValidationError("You cannot send an interest to yourself.")
        return data

    def get_requested_user(self, obj):
        try:
            user = User.objects.get(id=obj.sender.id)
            return user.username
        except User.DoesNotExist:
            return None
