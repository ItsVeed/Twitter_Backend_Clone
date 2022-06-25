# tweet/models.py

from ast import And
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import m2m_changed

User = get_user_model()

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    tweet = models.CharField(max_length=300, null=False, blank=False)
    datetimeuploaded = models.DateTimeField(auto_now_add=True, blank=True)
    users_liked = models.ManyToManyField(User, related_name='tweet_user_liked')
    likes = models.PositiveIntegerField(default=0)

def users_liked_changed(sender, instance, action, **kwargs):
    if action == "post_add":
        instance.likes += 1
    elif action == "post_remove":
        instance.likes -= 1

m2m_changed.connect(users_liked_changed, sender=Tweet.users_liked.through)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=False, blank=False)
    comment = models.CharField(max_length=250, null=False, blank=False)
    datetimeuploaded = models.DateTimeField(auto_now_add=True, blank=True)
    users_liked = models.ManyToManyField(User, related_name='comment_user_liked')
    likes = models.PositiveIntegerField(default=0)

def users_liked_changed(sender, instance, action, **kwargs):
    if action == "post_add":
        instance.likes += 1
    elif action == "post_remove":
        instance.likes -= 1

m2m_changed.connect(users_liked_changed, sender=Comment.users_liked.through)