from rest_framework import serializers
from .models import ContactForm


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the ContactForm model
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")

    class Meta:
        """
        Specify fields from ContactForm model
        """

        model = ContactForm
        fields = [
            "id",
            "owner",
            "subject",
            "message",
            "profile_id",
            "profile_image",
            "created_date",
            "updated_date",
        ]
