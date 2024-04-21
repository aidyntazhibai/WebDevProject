# users/views.py

from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import RegisterSerializer, ProfileModelSerializer
from .models import ProfileModel

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to register

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Override method to return the profile of the logged-in user
        return self.request.user.profilemodel

    # Additional methods and logic...
