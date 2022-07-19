from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/message/', include('message.urls')),
    path('api/v1/tweet/', include('tweet.urls'))
]
