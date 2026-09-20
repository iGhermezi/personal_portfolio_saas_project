from rest_framework import generics, permissions, serializers
from rest_framework.exceptions import NotFound

from .models import (
    Portfolio,
    Project,
    Skill,
    Education,
    Experience,
    SocialLink,
)

from .PortfolioSerializer import (
    PortfolioSerializer,
    ProjectSerializer,
    SkillSerializer,
    EducationSerializer,
    ExperienceSerializer,
    SocialLinkSerializer,
)

class PortfolioListCreateView(generics.ListCreateAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Portfolio.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class PortfolioDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Portfolio.objects.filter(
            user=self.request.user
        )


class PublicPortfolioDetailView(generics.RetrieveAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'slug'

    def get_queryset(self):
        return Portfolio.objects.filter(
            is_published=True
        )


class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Project.objects.filter(
            portfolio_id=self.kwargs['portfolio_pk'],
            portfolio__user=self.request.user
        )

    def perform_create(self, serializer):
        portfolio = Portfolio.objects.filter(
            pk=self.kwargs['portfolio_pk'],
            user=self.request.user
        ).first()

        if portfolio is None:
            raise NotFound('Portfolio not found.')

        serializer.save(
            portfolio=portfolio
        )


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Project.objects.filter(
            portfolio_id=self.kwargs['portfolio_pk'],
            portfolio__user=self.request.user
        )


class SkillListCreateView(generics.ListCreateAPIView):
    serializer_class = SkillSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Skill.objects.filter(
            portfolio_id=self.kwargs['portfolio_pk'],
            portfolio__user=self.request.user
        )

    def perform_create(self, serializer):
        portfolio = Portfolio.objects.filter(
            pk=self.kwargs['portfolio_pk'],
            user=self.request.user
        ).first()

        if portfolio is None:
            raise NotFound('Portfolio not found.')

        serializer.save(
            portfolio=portfolio
        )


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SkillSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Skill.objects.filter(
            portfolio_id=self.kwargs['portfolio_pk'],
            portfolio__user=self.request.user
        )


class EducationListCreateView(generics.ListCreateAPIView):
    serializer_class = EducationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Education.objects.filter(
            portfolio_id=self.kwargs['portfolio_pk'],
            portfolio__user=self.request.user
        )

    def perform_create(self, serializer):
        portfolio = Portfolio.objects.filter(
            pk=self.kwargs['portfolio_pk'],
            user=self.request.user
        ).first()

        if portfolio is None:
            raise NotFound('Portfolio not found.')

        serializer.save(
            portfolio=portfolio
        )


class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EducationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Education.objects.filter(
            portfolio_id=self.kwargs['portfolio_pk'],
            portfolio__user=self.request.user
        )


class ExperienceListCreateView(generics.ListCreateAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Experience.objects.filter(
            portfolio_id=self.kwargs['portfolio_pk'],
            portfolio__user=self.request.user
        )

    def perform_create(self, serializer):
        portfolio = Portfolio.objects.filter(
            pk=self.kwargs['portfolio_pk'],
            user=self.request.user
        ).first()

        if portfolio is None:
            raise NotFound('Portfolio not found.')

        serializer.save(
            portfolio=portfolio
        )


class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Experience.objects.filter(
            portfolio_id=self.kwargs['portfolio_pk'],
            portfolio__user=self.request.user
        )

class SocialLinkCreateView(generics.CreateAPIView):
    serializer_class = SocialLinkSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        portfolio = Portfolio.objects.filter(
            pk=self.kwargs['portfolio_pk'],
            user=self.request.user
        ).first()

        if portfolio is None:
            raise NotFound('Portfolio not found.')

        if SocialLink.objects.filter(
            portfolio=portfolio
        ).exists():
            raise serializers.ValidationError({
                'detail': 'Social link already exists.'
            })

        serializer.save(
            portfolio=portfolio
        )

class SocialLinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SocialLinkSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return SocialLink.objects.filter(
            portfolio_id=self.kwargs['portfolio_pk'],
            portfolio__user=self.request.user
        )