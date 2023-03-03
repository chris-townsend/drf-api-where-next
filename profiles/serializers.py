from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Profile


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

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

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

    class Meta:
        """
        Specify fields from Profile model
        """

        model = Profile
        fields = [
            'id', 'owner', 'created_date', 'updated_date', 'name', 'location',
            'favourite_location', 'date_of_birth', 'bio', 'is_owner',
        ]
