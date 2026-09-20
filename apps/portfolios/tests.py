from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework import status

from .models import (
    Portfolio,
    Project,
    Skill,
    Education,
    Experience,
    SocialLink,
)


User = get_user_model()


class PortfolioTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPassword123'
        )

        self.other_user = User.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='TestPassword123'
        )

        self.client.force_authenticate(
            user=self.user
        )

        self.portfolio = Portfolio.objects.create(
            user=self.user,
            title='My Portfolio',
            slug='my-portfolio',
            bio='My portfolio bio',
            is_published=False
        )

        self.other_portfolio = Portfolio.objects.create(
            user=self.other_user,
            title='Other Portfolio',
            slug='other-portfolio',
            bio='Other user portfolio',
            is_published=False
        )

    # --------------------------------------------------
    # Portfolio
    # --------------------------------------------------

    def test_user_can_create_portfolio(self):
        data = {
            'title': 'Second Portfolio',
            'slug': 'second-portfolio',
            'bio': 'Second portfolio bio',
            'is_published': False,
        }

        response = self.client.post(
            '/api/portfolios/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        portfolio = Portfolio.objects.get(
            slug='second-portfolio'
        )

        self.assertEqual(
            portfolio.user,
            self.user
        )

    def test_user_can_access_own_portfolio(self):
        response = self.client.get(
            f'/api/portfolios/{self.portfolio.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_cannot_access_other_users_portfolio(self):
        response = self.client.get(
            f'/api/portfolios/{self.other_portfolio.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    # --------------------------------------------------
    # Project
    # --------------------------------------------------

    def test_user_can_create_project_for_own_portfolio(self):
        data = {
            'pro_name': 'My Project',
            'pro_description': 'My project description',
            'pro_image': '',
            'pro_github_url': 'https://github.com/test/project',
            'pro_techs': 'Django, Python',
            'pro_live_demo_url': 'https://example.com',
            'pro_start': '2026-01-01',
            'pro_end': '2026-02-01',
        }

        response = self.client.post(
            f'/api/portfolios/{self.portfolio.id}/projects/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        project = Project.objects.get(
            pro_name='My Project'
        )

        self.assertEqual(
            project.portfolio,
            self.portfolio
        )

    def test_user_cannot_create_project_for_other_users_portfolio(self):
        data = {
            'pro_name': 'Unauthorized Project',
            'pro_description': 'Unauthorized',
            'pro_image': '',
            'pro_github_url': 'https://github.com/test/project',
            'pro_techs': 'Django',
            'pro_live_demo_url': 'https://example.com',
            'pro_start': '2026-01-01',
            'pro_end': '2026-02-01',
        }

        response = self.client.post(
            f'/api/portfolios/{self.other_portfolio.id}/projects/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    # --------------------------------------------------
    # Skill
    # --------------------------------------------------

    def test_user_can_create_skill_for_own_portfolio(self):
        data = {
            'skill_name': 'Python',
            'skill_level_in_skill': 5,
        }

        response = self.client.post(
            f'/api/portfolios/{self.portfolio.id}/skills/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        skill = Skill.objects.get(
            skill_name='Python'
        )

        self.assertEqual(
            skill.portfolio,
            self.portfolio
        )

    def test_user_cannot_create_skill_for_other_users_portfolio(self):
        data = {
            'skill_name': 'Unauthorized Skill',
            'skill_level_in_skill': 5,
        }

        response = self.client.post(
            f'/api/portfolios/{self.other_portfolio.id}/skills/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    # --------------------------------------------------
    # Education
    # --------------------------------------------------

    def test_user_can_create_education_for_own_portfolio(self):
        data = {
            'edu': 'University of Tehran',
        }

        response = self.client.post(
            f'/api/portfolios/{self.portfolio.id}/educations/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        education = Education.objects.get(
            edu='University of Tehran'
        )

        self.assertEqual(
            education.portfolio,
            self.portfolio
        )

    def test_user_cannot_create_education_for_other_users_portfolio(self):
        data = {
            'edu': 'Unauthorized Education',
        }

        response = self.client.post(
            f'/api/portfolios/{self.other_portfolio.id}/educations/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    # --------------------------------------------------
    # Experience
    # --------------------------------------------------

    def test_user_can_create_experience_for_own_portfolio(self):
        data = {
            'ex_company': 'Google',
            'ex_start_date': '2025-01-01',
            'ex_end_date': '2026-01-01',
            'ex_position': 'Backend Developer',
            'ex_description': 'Django backend development',
        }

        response = self.client.post(
            f'/api/portfolios/{self.portfolio.id}/experiences/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        experience = Experience.objects.get(
            ex_company='Google'
        )

        self.assertEqual(
            experience.portfolio,
            self.portfolio
        )

    def test_user_cannot_create_experience_for_other_users_portfolio(self):
        data = {
            'ex_company': 'Unauthorized Company',
            'ex_start_date': '2025-01-01',
            'ex_end_date': '2026-01-01',
            'ex_position': 'Developer',
            'ex_description': 'Unauthorized experience',
        }

        response = self.client.post(
            f'/api/portfolios/{self.other_portfolio.id}/experiences/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    # --------------------------------------------------
    # SocialLink
    # --------------------------------------------------

        # SocialLink

    def test_user_can_create_social_link_for_own_portfolio(self):
        data = {
            'sl_github': 'https://github.com/testuser',
            'sl_linkedin': 'https://linkedin.com/in/testuser',
            'sl_personal_web': 'https://testuser.com',
        }

        response = self.client.post(
            f'/api/portfolios/{self.portfolio.id}/social-links/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        social_link = SocialLink.objects.get(
            portfolio=self.portfolio
        )

        self.assertEqual(
            social_link.portfolio,
            self.portfolio
        )

    def test_user_cannot_create_social_link_for_other_users_portfolio(self):
        data = {
            'sl_github': 'https://github.com/other',
            'sl_linkedin': 'https://linkedin.com/in/other',
            'sl_personal_web': 'https://other.com',
        }

        response = self.client.post(
            f'/api/portfolios/{self.other_portfolio.id}/social-links/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

        self.assertFalse(
            SocialLink.objects.filter(
                portfolio=self.other_portfolio
            ).exists()
        )