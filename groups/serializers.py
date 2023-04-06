from django.contrib.humanize.templatetags.humanize import naturaltime
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    """
    Group serializer which converts Group model into JSON
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    members = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True)
    created_date = serializers.SerializerMethodField()
    is_member = serializers.SerializerMethodField()

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

    class Meta:
        model = Group
        fields = ['id', 'owner', 'group_name', 'description',
                  'created_date', 'members', 'is_member']
