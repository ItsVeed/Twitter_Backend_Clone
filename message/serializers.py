# message/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()

class CreateMeassageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('message',)

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('message', 'sender', 'recipient')
