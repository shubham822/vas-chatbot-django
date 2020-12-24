from rest_framework import serializers
from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our profile object."""

    class Meta:
        model = models.UserProfile
        fields = ('rno', 'name', 'sem', 'division', 'password')
        lookup_field = 'rno'
        extra_kwargs = {
            'last_login': {'read_only': True},
            'password': {'write_only': True},
            'url': {'lookup_field': 'rno'}
        }

    def create(self, validated_data):
        """Used to create a new user."""

        user = models.UserProfile(
            rno=validated_data['rno'],
            name=validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    Serializer for password change endpoint.
    """
    class Meta:
        model = models.UserProfile
        fields = ('passw',)
        lookup_field = 'rno'
        extra_kwargs = {
            'url': {'lookup_field': 'rno'}
        }

class UserInfoSerializer(serializers.ModelSerializer):
    """A serializer for user info."""

    class Meta:
        model = models.UserProfile
        fields = ('rno', 'name', 'batch', 'workshop', 'sports', 'creative', 'cultural', 'placement', 'dance', 'drama', 'study')
        read_only_fields = ('rno', 'name',)
        lookup_field = 'rno'
        extra_kwargs = {
            'url': {'lookup_field': 'rno'}
        }

class QuerySerializer(serializers.Serializer):
    """Query Serializer"""

    query = serializers.CharField(allow_blank=False)

class NotifSerializer(serializers.ModelSerializer):
    """Group Notif Serializer"""

    class Meta:
        model = models.Information
        fields = ('notification', 'interest', 'date', 'filepresent', 'filename')

class IndividualNotifSerializer(serializers.ModelSerializer):
    """Individual Notif Serializer"""

    class Meta:
        model = models.Individual
        fields = ('rollno', 'notice', 'interest', 'date')

class SupportSerializer(serializers.ModelSerializer):
    """Support Serializer"""

    class Meta:
        model = models.Support
        fields = ('subject', 'details', 'rno', 'name')