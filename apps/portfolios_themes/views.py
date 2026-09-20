from rest_framework import generics, permissions
from .models import PortfolioTemplate
from .serializers import PortfolioTemplateSerializer

class PortfolioTemplateListView(generics.ListAPIView):
    queryset = PortfolioTemplate.objects.filter(is_active=True)
    serializer_class = PortfolioTemplateSerializer
    permission_classes = (permissions.AllowAny,)