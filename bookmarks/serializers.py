from django.db import IntegrityError
from rest_framework import serializers
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    """
    Bookmark serializer which converts Bookmark model into JSON
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bookmark
        fields = ['id', 'owner', 'post', 'created_date']

    def create(self, validated_data):
        """
        If a user tries to bookmark the same post multiple times,
        it will throw a duplicate error
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplication'
            })
