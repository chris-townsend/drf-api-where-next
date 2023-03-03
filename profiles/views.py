from django.db.models import Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from where_next_drf_api.permissons import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    ProfileList generic class which lists all Profiles,
    Profile creation is handled by Django signals
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_date')
    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_date',
        'owner__followed__created_date',
        ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_date')
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
