from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Comment serializer class converts to JSON
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_date = serializers.SerializerMethodField()
    updated_date = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Checks if the requested user is the owner of the comment
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_date(self, obj):
        """
        Displays the created date of the comment
        """
        return naturaltime(obj.created_date)

    def get_updated_date(self, obj):
        """
        Displays the last updated date of the comment
        """
        return naturaltime(obj.updated_date)

    class Meta:
        """
        Specify fields from Comment model
        """
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_date', 'updated_date', 'comment']
