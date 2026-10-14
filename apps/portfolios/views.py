from rest_framework import generics, permissions, serializers
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


from .models import (
    Portfolio,
    Project,
    Skill,
    Education,
    Experience,
    SocialLink,
)

from .portfolio_serializer import (
    PortfolioSerializer,
    PublicPortfolioSerializer,
    ProjectSerializer,
    SkillSerializer,
    EducationSerializer,
    ExperienceSerializer,
    SocialLinkSerializer,
)
class PortfolioListCreateView(generics.ListCreateAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get_queryset(self):
        return Portfolio.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        if Portfolio.objects.filter(user=self.request.user).exists():
            raise serializers.ValidationError(
                'You already have a portfolio.'
            )

        serializer.save(user=self.request.user)

class PortfolioDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get_queryset(self):
        return Portfolio.objects.filter(
            user=self.request.user
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        allowed_data = {}

        for field in self.get_serializer().fields:
            if field in request.data:
                allowed_data[field] = request.data[field]

        serializer = self.get_serializer(
            instance,
            data=allowed_data,
            partial=partial,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class PublicPortfolioDetailView(generics.RetrieveAPIView):
    serializer_class = PublicPortfolioSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'slug'

    def get_queryset(self):
        return Portfolio.objects.filter(is_published=True)

class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (JSONParser, MultiPartParser, FormParser)

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

    def create(self, request, *args, **kwargs):
        allowed_data = {}
        for field in self.get_serializer().fields:
            if field in request.data:
                allowed_data[field] = request.data[field]

        serializer = self.get_serializer(data=allowed_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (JSONParser, MultiPartParser, FormParser)

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

    def get(self, request, portfolio_pk):
        social = SocialLink.objects.filter(
            portfolio_id=portfolio_pk,
            portfolio__user=request.user,
        ).first()

        if social is None:
            raise NotFound('Social link not found.')

        return Response(
            self.get_serializer(social).data
        )

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

class SocialLinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SocialLinkSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return SocialLink.objects.filter(
            portfolio_id=self.kwargs['portfolio_pk'],
            portfolio__user=self.request.user
        )