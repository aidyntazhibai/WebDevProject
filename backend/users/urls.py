# users/urls.py

from django.urls import path
from .views import RegisterView, ProfileView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/profile/', ProfileView.as_view(), name='profile'),
]
