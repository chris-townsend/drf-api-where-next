from rest_framework import generics, permissions
from where_next_drf_api.permissons import IsOwnerOrReadOnly
from .models import Group
from .serializers import GroupSerializer


class GroupList(generics.ListCreateAPIView):
    """
    List groups, create a group if the user is logged in
    perform_create method automatically set the owner to the
    user who is creating the group
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
