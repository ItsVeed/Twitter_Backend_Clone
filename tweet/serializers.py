# tweet/serializers.py

from rest_framework import serializers
from .models import Tweet

class CreateTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('tweet',)

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('user', 'tweet', 'datetimeuploaded', 'likes')