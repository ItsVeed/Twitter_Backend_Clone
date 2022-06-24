# message/models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', null=False, blank=False)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient', null=False, blank=False)
    datetimesent = models.DateTimeField(auto_now_add=True, blank=True)
    message = models.CharField(max_length=300, null=False, blank=False)
