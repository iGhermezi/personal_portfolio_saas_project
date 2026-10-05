from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser

from .models import PortfolioTemplate
from .serializers import PortfolioTemplateSerializer


class PortfolioTemplateListView(generics.ListAPIView):
    serializer_class = PortfolioTemplateSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        return PortfolioTemplate.objects.filter(
            is_active=True
        ).order_by('id')


class PortfolioTemplateDetailView(generics.RetrieveAPIView):
    serializer_class = PortfolioTemplateSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        return PortfolioTemplate.objects.filter(
            is_active=True
        )