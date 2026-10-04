from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from rest_framework import serializers


User = get_user_model()


class EmailVerificationSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()

    def validate(self, attrs):
        try:
            uid = force_str(
                urlsafe_base64_decode(
                    attrs['uid']
                )
            )

            user = User.objects.get(
                pk=uid
            )

        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
        ):
            raise serializers.ValidationError({
                'token': 'Invalid email verification link.'
            })

        if user.email_verified:
            raise serializers.ValidationError({
                'token': 'Email is already verified.'
            })

        token_generator = PasswordResetTokenGenerator()

        if not token_generator.check_token(
            user,
            attrs['token']
        ):
            raise serializers.ValidationError({
                'token': 'Invalid or expired email verification link.'
            })

        attrs['user'] = user

        return attrs