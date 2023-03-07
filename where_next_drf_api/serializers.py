from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer for the CurrentUser which retrieves profile_id & profile_image
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image')
