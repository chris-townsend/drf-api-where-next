from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer class inheriting from ModelSerializer class,
    Specify owner as read only so it can't be edited, populate with owners username
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        Specify fields from Profile model
        """
        model = Profile
        fields = [
            'id', 'owner', 'created_date', 'updated_date', 'name', 'location',
            'favourite_location', 'bio', 'profile_image'
        ]
