from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from where_next_drf_api.permissons import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    ProfileList generic class which lists all Profiles,
    Profile creation is handled by Django signals
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
