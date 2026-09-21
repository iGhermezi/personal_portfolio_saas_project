from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()


class EmailLoginSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'] = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        try:
            user = User.objects.get(
                email__iexact=email
            )

        except User.DoesNotExist:
            raise serializers.ValidationError({
                'detail': 'Invalid email or password.'
            })

        if not user.check_password(password):
            raise serializers.ValidationError({
                'detail': 'Invalid email or password.'
            })

        if not user.is_active:
            raise serializers.ValidationError({
                'detail': 'account has been banned !'
            })

        if not user.email_verified:
            raise serializers.ValidationError({
                'detail': 'email address is not verified'
            })

        refresh = self.get_token(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'email': user.email,
                'username': user.username,
            }
        }