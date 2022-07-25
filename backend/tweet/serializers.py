# tweet/serializers.py

from rest_framework import serializers
from .models import Tweet, Comment, User

class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('tweet', 'comment')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'datetimeuploaded', 'likes', 'comment')

class CreateTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('tweet',)

class TweetSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    # comments = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ('pk', 'user', 'tweet', 'datetimeuploaded', 'likes', 'comments')
    
    # def get_comments(self, obj):
    #     tweet_comment_query = Comment.objects.filter(tweet=obj.id)
    #     serializer = CommentSerializer(tweet_comment_query, many=True)

    #     return serializer.data