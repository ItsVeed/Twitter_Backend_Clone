from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/auth/', include('authentication.urls')),
    path('api/message/', include('message.urls')),
    path('api/tweet/', include('tweet.urls'))
]
