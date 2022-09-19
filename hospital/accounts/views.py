from .models import CustomUser, Profile
from .serializers import CustomUserSerializer, UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User

from .permissions import IsOwner


class UserProfileDetailView(generics.RetrieveAPIView):
    """[summary]
    User can view his profile information.

    [restrictions]
    Only super user and owner can view the profile information.
    Later(Allow member of the company to view the profile information of another member)

    """

    permission_classes = (IsOwner,)
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.all()


class UserProfileCreateView(generics.CreateAPIView):
    """[summary]
    - Create user profile 
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserProfileUpdateView(generics.UpdateAPIView):
    """
    [summary]
    - Update user profile information

    [restrictions]:
    - USER can't change profile information of another user.
    """

    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner,
    )
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.all()
