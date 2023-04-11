from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer class inheriting from ModelSerializer class,
    Specify owner as read only so it can't be edited,
    populate with owners username
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    created_date = serializers.SerializerMethodField()
    updated_date = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    bookmarks_count = serializers.ReadOnlyField()
    groups_count = serializers.ReadOnlyField()
    date_of_birth = serializers.DateField(format="%Y-%m-%d")

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Display a users current following count and following id
        if the user is logged-in, else the field will display null
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user,
                followed=obj.owner
            ).first()
            return following.id if following else None
        return None

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

    def get_groups_count(self, obj):
        """
        Returns the number of groups the profile's owner is a member of
        """
        return obj.owner.groups.count()

    class Meta:
        """
        Specify fields from Profile model
        """

        model = Profile
        fields = [
            'id', 'owner', 'created_date', 'updated_date', 'name', 'location',
            'favourite_location', 'date_of_birth', 'bio', 'image', 'is_owner',
            'following_id', 'posts_count', 'following_count',
            'followers_count', 'bookmarks_count', 'groups_count'
        ]
