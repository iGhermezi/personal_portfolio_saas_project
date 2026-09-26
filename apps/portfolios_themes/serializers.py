from rest_framework import serializers

from .models import PortfolioTemplate


class PortfolioTemplateSerializer(serializers.ModelSerializer):
    can_use = serializers.SerializerMethodField()
    lock_reason = serializers.SerializerMethodField()

    class Meta:
        model = PortfolioTemplate
        fields = (
            'id',
            'name',
            'description',
            'preview_img',
            'template_key',
            'access_level',
            'is_active',
            'can_use',
            'lock_reason',
        )

    def _get_user(self):
        request = self.context.get('request')

        if request and request.user.is_authenticated:
            return request.user

        return None

    def get_can_use(self, obj):
        user = self._get_user()

        if not user:
            return False

        if obj.access_level == PortfolioTemplate.ACCESS_FREE:
            return True

        if obj.access_level == PortfolioTemplate.ACCESS_VERIFIED:
            return user.email_verified

        if obj.access_level == PortfolioTemplate.ACCESS_PREMIUM:
            return user.has_active_subscription

        return False

    def get_lock_reason(self, obj):
        if self.get_can_use(obj):
            return None

        if obj.access_level == PortfolioTemplate.ACCESS_VERIFIED:
            return 'verification'

        if obj.access_level == PortfolioTemplate.ACCESS_PREMIUM:
            return 'subscription'

        return 'unavailable'