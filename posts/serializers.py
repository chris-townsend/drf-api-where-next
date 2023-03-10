from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Post
from likes.models import Like
from comments.models import Comment
from bookmarks.models import Bookmark


class PostSerializer(serializers.ModelSerializer):
    """
    Post serializer class inheriting from ModelSerializer,
    Specify owner as read only so it can't be edited,
    populate with owners username
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_date = serializers.SerializerMethodField()
    updated_date = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    comment_id = serializers.SerializerMethodField()
    bookmark_count = serializers.ReadOnlyField()
    bookmark_id = serializers.SerializerMethodField()

    def get_created_date(self, obj):
        """
        Returns a human readable time for created profile date
        """
        return naturaltime(obj.created_date)

    def get_updated_date(self, obj):
        """
        Returns a human readable time for updated profile date
        """
        return naturaltime(obj.updated_date)

    def validate_image(self, value):
        """
        Image validation function
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Image size too big! Must be smaller than 2MB')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Display a users current like count and like id
        if the user is logged-in, else the field will display null
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user,
                post=obj
            ).first()
            return like.id if like else None

        return None

    def get_comment_id(self, obj):
        """
        Display a users current comment count and comment id
        if the user is logged-in, else the field will display null
        """
        user = self.context['request'].user
        if user.is_authenticated:
            comment = Comment.objects.filter(
                owner=user,
                post=obj
            ).first()
            return comment.id if comment else None

        return None

    def get_bookmark_id(self, obj):
        """
        Display a users current bookmark count and bookmark id
        if the user is logged-in, else the field will display null
        """
        user = self.context['request'].user
        if user.is_authenticated:
            bookmark = Bookmark.objects.filter(
                owner=user,
                post=obj
            ).first()
            return bookmark.id if bookmark else None

        return None

    class Meta:
        """
        Specify fields from Post model
        """
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_date', 'updated_date', 'title', 'about', 'image',
            'like_id', 'likes_count', 'comments_count', 'bookmark_count',
            'comment_id', 'bookmark_id'
        ]
