from rest_framework import serializers


class EmailVerificationResendSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        return value.lower().strip()