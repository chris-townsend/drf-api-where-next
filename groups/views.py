from rest_framework import generics, permissions, status
from rest_framework.response import Response
from where_next_drf_api.permissions import IsOwnerOrReadOnly
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


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update & delete a group if you're the owner.
    """
    queryset = Group.objects.all().order_by('-created_date')
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = GroupSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class JoinGroupView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GroupSerializer

    def get(self, request, pk=None):
        group = Group.objects.get(pk=pk)
        user = request.user
        if user in group.members.all():
            return Response(
                {"detail": "You are already a member of this group."},
                status=status.HTTP_400_BAD_REQUEST)
        group.members.add(user)
        group.save()
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def post(self, request, pk=None):
        return self.get(request, pk)

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj

    def get_queryset(self):
        return Group.objects.all()


class LeaveGroupView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GroupSerializer

    def delete(self, request, pk=None):
        group = Group.objects.get(pk=pk)
        user = request.user
        if user not in group.members.all():
            return Response(
                {"detail": "You are not a member of this group."},
                status=status.HTTP_400_BAD_REQUEST)
        group.members.remove(user)
        group.save()
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj

    def get_queryset(self):
        return Group.objects.all()
