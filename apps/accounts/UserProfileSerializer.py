from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'profile_image_url',
            'job_title',
            'phone',
            'location',
            'email_verified',
            'has_active_subscription',
            )
        read_only_fields = (
            'id',
            'email',
            'email_verified',
            'has_active_subscription',
            )