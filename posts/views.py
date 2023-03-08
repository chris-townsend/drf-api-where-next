from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from .models import Post
from .serializers import PostSerializer
from where_next_drf_api.permissons import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    List posts or if the user is logged-in they have the ability to
    create posts. perform_create method associates the post
    with the logged-in user
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
        bookmark_count=Count('bookmark', distinct=True)
    ).order_by('-created_date')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    search_fields = [
        'title',
        'owner__username',
    ]

    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_date',
    ]

    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'bookmark__owner__profile',
        'owner__profile',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and have the ability to edit or delete if you are the
    owner of the post
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
        bookmark_count=Count('bookmark', distinct=True)
    ).order_by('-created_date')
