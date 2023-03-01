from rest_framework import serializers
from .models import Post


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

    def validate_image(self, value):
        """
        Image validation function
        """
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size too big, must be below 2MB!')
            if value.image.width > 4096:
                raise serializers.ValidationError(
                    'Image width larger than 4096px!')
            if value.image.height > 4096:
                raise serializers.ValidationError(
                    'Image height larger than 4096px!')

            return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Specify fields from Post model
        """

        model = Post
        fields = [
            'id', 'owner', 'created_date', 'updated_date', 'location',
            'favourite_location', 'bio', 'profile_image', 'is_owner',
            'profile_id', 'title', 'image'
        ]
