# tweet/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreateTweet.as_view(), name='tweet'),
    path('<int:pk>/', views.RetrieveTweet.as_view(), name='retrieve_tweet'),
    path('<int:pk>/delete/', views.DeleteTweet.as_view(), name='delete_tweet'),
    path('<int:pk>/like/', views.LikeTweet, name='like_tweet')
]