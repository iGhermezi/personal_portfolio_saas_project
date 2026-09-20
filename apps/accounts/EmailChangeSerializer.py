from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailChangeRequestSerializer(serializers.Serializer):
    new_email = serializers.EmailField()

    def validate_new_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("this email already in use")
        return value


class EmailChangeConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6, min_length=6)