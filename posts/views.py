from django.db.models import Count
from rest_framework import generics, permissions
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
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_date')

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
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_date')
