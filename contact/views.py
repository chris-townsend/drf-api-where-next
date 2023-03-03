from rest_framework import generics, permissions
from .models import ContactForm
from .serializers import ContactSerializer
from where_next_drf_api.permissons import IsOwnerOrReadOnly


class ContactList(generics.ListCreateAPIView):
    """
    List messages or create a message if the user is logged-in
    """
    queryset = ContactForm.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a message and delete it by id if the user is
    logged-in as admin
    """
    queryset = ContactForm.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAdminUser]
