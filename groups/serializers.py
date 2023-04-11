from django.contrib.humanize.templatetags.humanize import naturaltime
from django.contrib.auth.models import User
from rest_framework import serializers
from profiles.serializers import ProfileSerializer
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    """
    Group serializer which converts Group model into JSON
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_profile = ProfileSerializer(source='owner.profile', read_only=True)
    members = ProfileSerializer(many=True, read_only=True)
    created_date = serializers.SerializerMethodField()
    is_member = serializers.SerializerMethodField()
    groups_count = serializers.SerializerMethodField()

    def get_created_date(self, obj):
        """
        Returns a human readable time for created date
        """
        return naturaltime(obj.created_date)

    def get_is_member(self, obj):
        """
        Returns a boolean indicating if the authenticated
        user is a member of the group
        """
        user = self.context['request'].user
        return user in obj.members.all()

    def get_groups_count(self, obj):
        """
        Returns the number of groups the profile's owner is a member of
        """
        return obj.owner.groups.count()

    class Meta:
        model = Group
        fields = ['id', 'owner', 'group_name', 'description',
                  'created_date', 'members', 'is_member', 'owner_profile']
