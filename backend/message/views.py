# message/views.py

from http.client import ResponseNotReady
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q
from django.contrib.auth import get_user_model

from .models import Message
from .serializers import MessageSerializer, CreateMeassageSerializer

User = get_user_model()

class ListCreateMessage(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Message.objects.filter(Q(sender=user) | Q(recipient=user))
        return queryset
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateMeassageSerializer
        else:
            return MessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        recipient = User.objects.filter(username=self.request.POST['recipient_username']).first()
        if recipient != None:
            self.perform_create(serializer, recipient)
            return Response(data={"message": "Message was successfully sent."}, status=status.HTTP_201_CREATED)
        return Response(data={"message": "The user you are trying to message does not exist."}, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer, recipient):
        user = self.request.user    
        serializer.save(sender=user, recipient=recipient)

class RetrieveMessage(generics.RetrieveAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Message.objects.filter(Q(sender=user) | Q(recipient=user))
        return queryset
