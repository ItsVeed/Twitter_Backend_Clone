# authentication/models.py

from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser
from ..tweet.models import Tweet

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, db_index=True, primary_key=True)
    email = models.EmailField(max_length=254)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']