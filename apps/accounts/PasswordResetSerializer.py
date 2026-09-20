from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


User = get_user_model()


class PasswordResetSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(
        write_only=True,
        min_length=8
    )
    confirm_password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                'confirm_password': "passwords do not match"
            })

        try:
            uid = force_str(
                urlsafe_base64_decode(attrs['uid'])
            )
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise serializers.ValidationError({
                'token': "link is invalid"
            })

        token_generator = PasswordResetTokenGenerator()

        if not token_generator.check_token(user, attrs['token']):
            raise serializers.ValidationError({
                'token': "link is invalid or expired"
            })

        validate_password(
            attrs['new_password'],
            user=user
        )

        attrs['user'] = user

        return attrs