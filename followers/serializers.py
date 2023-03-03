from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Follower serializer which converts Follower model into JSON
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')
    created_date = serializers.SerializerMethodField()

    def get_created_date(self, obj):
        """
        Returns a human readable time for follower date
        """
        return naturaltime(obj.created_date)

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'created_date', 'followed', 'followed_name'
        ]

    def create(self, validated_data):
        """
        Prevents a user from following the same user multiple times,
        it will throw a duplication error.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplication'
            })
