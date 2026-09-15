from rest_framework import generics, permissions
from .models import Portfolio, Project, Skill
from .PortfolioSerializer import (
    PortfolioSerializer, ProjectSerializer, SkillSerializer,
)


# ==============================
# ۱. مدیریت پورتفولیوها
# ==============================
class PortfolioListCreateView(generics.ListCreateAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PortfolioDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)


class PublicPortfolioDetailView(generics.RetrieveAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'slug'

    def get_queryset(self):
        return Portfolio.objects.filter(is_published=True)


# ==============================
# ۲. مدیریت پروژه‌ها (Nested زیر یک Portfolio مشخص)
# ==============================
class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Project.objects.filter(
            portfolio_id=self.kwargs['portfolio_pk'],
            portfolio__user=self.request.user
        )

    def perform_create(self, serializer):
        portfolio = Portfolio.objects.get(
            pk=self.kwargs['portfolio_pk'],
            user=self.request.user
        )
        serializer.save(portfolio=portfolio)


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Project.objects.filter(
            portfolio_id=self.kwargs['portfolio_pk'],
            portfolio__user=self.request.user
        )


# ==============================
# ۳. مدیریت مهارت‌ها (Nested زیر یک Portfolio مشخص)
# ==============================
class SkillListCreateView(generics.ListCreateAPIView):
    serializer_class = SkillSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Skill.objects.filter(
            portfolio_id=self.kwargs['portfolio_pk'],
            portfolio__user=self.request.user
        )

    def perform_create(self, serializer):
        portfolio = Portfolio.objects.get(
            pk=self.kwargs['portfolio_pk'],
            user=self.request.user
        )
        serializer.save(portfolio=portfolio)


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SkillSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Skill.objects.filter(
            portfolio_id=self.kwargs['portfolio_pk'],
            portfolio__user=self.request.user
        )