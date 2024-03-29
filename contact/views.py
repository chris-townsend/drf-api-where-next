from rest_framework import generics, permissions
from .models import ContactForm
from .serializers import ContactFormSerializer
from where_next_drf_api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAdminUser


class ContactList(generics.ListCreateAPIView):
    """
    List messages or create a message if the user is logged-in
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a message and delete it by id if the user is the owner
    of the message or an admin user
    """
    permission_classes = [permissions.IsAdminUser]
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
