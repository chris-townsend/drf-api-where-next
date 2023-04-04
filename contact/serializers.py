from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import ContactForm


class ContactFormSerializer(serializers.ModelSerializer):
    """
    Serializer for the ContactForm model
    """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_date = serializers.SerializerMethodField()
    updated_date = serializers.SerializerMethodField()

    def get_created_date(self, obj):
        """
        Displays the created date of the message
        """
        return naturaltime(obj.created_date)

    def get_updated_date(self, obj):
        """
        Displays the last updated date of the message
        """
        return naturaltime(obj.updated_date)

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
