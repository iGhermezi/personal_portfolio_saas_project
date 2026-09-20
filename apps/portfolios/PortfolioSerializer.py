from rest_framework import serializers
from .models import Portfolio, Project, Skill, Education, Experience, SocialLink


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('portfolio',)


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        read_only_fields = ('portfolio',)


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
        read_only_fields = ('portfolio',)


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
        read_only_fields = ('portfolio',)


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'
        read_only_fields = ('portfolio',)

class PortfolioSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True, source='project')
    skills = SkillSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    social = SocialLinkSerializer(read_only=True)

    class Meta:
        model = Portfolio
        fields = (
            'id', 'user', 'template', 'title', 'slug', 'bio', 
            'is_published', 'created_at', 'updated_at',
            'projects', 'skills', 'educations', 'experiences', 'social'
        )
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')