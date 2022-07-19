# tweet/views.py

from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TweetSerializer, CreateTweetSerializer, CommentSerializer, CreateCommentSerializer
from .models import Tweet, Comment

class ListCreateTweet(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateTweetSerializer
        else:
            return TweetSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class RetrieveTweet(generics.RetrieveAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticated]

class DeleteTweet(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Tweet.objects.filter(user=self.request.user)
        return queryset

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def LikeTweet(request, pk):
    try:
        tweet = Tweet.objects.get(pk=pk)
    except Tweet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if tweet.users_liked.filter(username=request.user.username).exists():
        tweet.users_liked.remove(request.user)
        tweet.save()
        return Response(status=status.HTTP_200_OK)
    else:
        tweet.users_liked.add(request.user)
        tweet.save()
        return Response(status=status.HTTP_200_OK)


class CreateComment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class DeleteComment(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Comment.objects.filter(user=self.request.user)
        return queryset

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def LikeComment(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if comment.users_liked.filter(username=request.user.username).exists():
        comment.users_liked.remove(request.user)
        comment.save()
        return Response(status=status.HTTP_200_OK)
    else:
        comment.users_liked.add(request.user)
        comment.save()
        return Response(status=status.HTTP_200_OK)