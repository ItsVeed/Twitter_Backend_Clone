# message/urls.py

from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.ListCreateMessage.as_view(), name='message'),
    path('<int:pk>/', views.RetrieveMessage.as_view(), name='retrieve_message')
]