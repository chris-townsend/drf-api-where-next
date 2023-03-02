from rest_framework import generics, permissions
from where_next_drf_api.permissons import IsOwnerOrReadOnly
from .models import Bookmark
from .serializers import BookmarkSerializer


class BookmarkList(generics.ListCreateAPIView):
    """
    Posts can be bookmarked by a logged-in user
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarkDetail(generics.RetrieveDestroyAPIView):
    """
    Bookmarks can be retrieved and deleted
    """
    serializer_class = BookmarkSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Bookmark.objects.all()
