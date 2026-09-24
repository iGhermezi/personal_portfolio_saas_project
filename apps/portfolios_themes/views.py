from rest_framework import generics, permissions

from .models import PortfolioTemplate
from .serializers import PortfolioTemplateSerializer


class PortfolioTemplateListView(generics.ListAPIView):
    serializer_class = PortfolioTemplateSerializer

    def get_permissions(self):
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user

        queryset = PortfolioTemplate.objects.filter(
            is_active=True
        )

        if user.has_active_subscription:
            return queryset

        if user.email_verified:
            return queryset.exclude(
                access_level=PortfolioTemplate.ACCESS_PREMIUM
            )

        return queryset.filter(
            access_level=PortfolioTemplate.ACCESS_FREE
        )