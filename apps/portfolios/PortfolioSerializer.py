
from rest_framework import serializers

from .models import (
    Portfolio,
    Project,
    Skill,
    Education,
    Experience,
    SocialLink,
)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('id', 'portfolio')

    def validate(self, attrs):
        start_date = attrs.get('pro_start')
        end_date = attrs.get('pro_end')

        if start_date and end_date and end_date < start_date:
            raise serializers.ValidationError({
                'pro_end': 'Project end date cannot be before start date.'
            })

        return attrs

    def validate_pro_github_url(self, value):
        if not value.startswith(('http://', 'https://')):
            raise serializers.ValidationError(
                'GitHub URL must start with http:// or https://.'
            )

        return value

    def validate_pro_live_demo_url(self, value):
        if value and not value.startswith(('http://', 'https://')):
            raise serializers.ValidationError(
                'Live demo URL must start with http:// or https://.'
            )

        return value


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        read_only_fields = ('id', 'portfolio')

    def validate_skill_level_in_skill(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError(
                'Skill level must be between 1 and 5.'
            )

        return value


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
        read_only_fields = ('id', 'portfolio')


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
        read_only_fields = ('id', 'portfolio')

    def validate(self, attrs):
        start_date = attrs.get('ex_start_date')
        end_date = attrs.get('ex_end_date')

        if start_date and end_date and end_date < start_date:
            raise serializers.ValidationError({
                'ex_end_date': (
                    'Experience end date cannot be before start date.'
                )
            })

        return attrs


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'
        read_only_fields = ('id', 'portfolio')

    def validate(self, attrs):
        url_fields = (
            'sl_github',
            'sl_linkedin',
            'sl_personal_web',
        )

        errors = {}

        for field in url_fields:
            value = attrs.get(field)

            if value and not value.startswith(('http://', 'https://')):
                errors[field] = (
                    'URL must start with http:// or https://.'
                )

        if errors:
            raise serializers.ValidationError(errors)

        return attrs


class PortfolioSerializer(serializers.ModelSerializer):
    template_key = serializers.SerializerMethodField()

    projects = ProjectSerializer(
        many=True,
        read_only=True
    )
    skills = SkillSerializer(
        many=True,
        read_only=True
    )
    educations = EducationSerializer(
        many=True,
        read_only=True
    )
    experiences = ExperienceSerializer(
        many=True,
        read_only=True
    )
    social = SocialLinkSerializer(
        read_only=True
    )
    def get_template_key(self, obj):
        if not obj.template:
            return None

        return obj.template.template_key

    class Meta:
        model = Portfolio
        fields = (
            'id',
            'user',
            'template',
            'template_key',
            'title',
            'slug',
            'bio',
            'is_published',
            'created_at',
            'updated_at',
            'projects',
            'skills',
            'educations',
            'experiences',
            'social',
        )   

        read_only_fields = (
            'id',
            'user',
            'created_at',
            'updated_at',
        )

    def validate_title(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                'Title cannot be empty.'
            )

        return value

    def validate_slug(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                'Slug cannot be empty.'
            )

        return value

    def validate_template(self, value):
        user = self.context['request'].user

        if not value.is_active:
            raise serializers.ValidationError(
                'This template is not available.'
            )

        if value.access_level == 'free':
            return value

        if value.access_level == 'premium':
            if not user.has_active_subscription:
                raise serializers.ValidationError(
                    'An active subscription is required for this template.'
                )

            return value

        raise serializers.ValidationError(
            'Invalid template access level.'
        )

class PublicPortfolioSerializer(serializers.ModelSerializer):
    template_key = serializers.SerializerMethodField()

    projects = ProjectSerializer(
        many=True,
        read_only=True
    )
    skills = SkillSerializer(
        many=True,
        read_only=True
    )
    educations = EducationSerializer(
        many=True,
        read_only=True
    )
    experiences = ExperienceSerializer(
        many=True,
        read_only=True
    )
    social = SocialLinkSerializer(
        read_only=True
    )
    def get_template_key(self, obj):
        if not obj.template:
            return None

        return obj.template.template_key

    class Meta:
        model = Portfolio
        fields = (
        'id',
        'template',
        'template_key',
        'title',
        'slug',
        'bio',
        'is_published',
        'created_at',
        'updated_at',
        'projects',
        'skills',
        'educations',
        'experiences',
        'social',
         )
        read_only_fields = fields
