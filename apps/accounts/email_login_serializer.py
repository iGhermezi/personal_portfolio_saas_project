from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .user_profile_serializer import UserProfileSerializer


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

        refresh = self.get_token(user)
        profile_data = UserProfileSerializer(
            user,
            context=self.context,
        ).data

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'email': user.email,
                'username': user.username,
                'email_verified': user.email_verified,
                'has_active_subscription': user.has_active_subscription,
                'profile_image': profile_data['profile_image'],
                'profile_image_url': profile_data['profile_image_url'],
}
        }