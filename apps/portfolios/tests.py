from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory

from types import SimpleNamespace

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import SimpleTestCase
from django.test.utils import override_settings
from PIL import Image

from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework import status

from .models import (
    Portfolio,
    Project,
    Skill,
    Education,
    Experience,
    SocialLink,
)
from .portfolio_serializer import PortfolioSerializer


User = get_user_model()


def uploaded_project_image(name):
    image_buffer = BytesIO()
    Image.new('RGB', (1, 1)).save(image_buffer, format='PNG')
    return SimpleUploadedFile(
        name,
        image_buffer.getvalue(),
        content_type='image/png',
    )


class PortfolioTemplatePreviewSerializerTests(SimpleTestCase):

    def setUp(self):
        request = APIRequestFactory().get('/api/portfolios/')
        self.serializer = PortfolioSerializer(
            context={'request': request}
        )

    def test_returns_preview_image_from_each_portfolios_template(self):
        first_portfolio = SimpleNamespace(
            template=SimpleNamespace(
                preview_image=SimpleNamespace(
                    url='/media/template_previews/first.jpg'
                )
            )
        )
        second_portfolio = SimpleNamespace(
            template=SimpleNamespace(
                preview_image=SimpleNamespace(
                    url='/media/template_previews/second.jpg'
                )
            )
        )

        self.assertEqual(
            self.serializer.get_template_preview_image(first_portfolio),
            'http://testserver/media/template_previews/first.jpg',
        )
        self.assertEqual(
            self.serializer.get_template_preview_image(second_portfolio),
            'http://testserver/media/template_previews/second.jpg',
        )

    def test_returns_none_without_template_or_preview_image(self):
        without_template = SimpleNamespace(template=None)
        without_preview_image = SimpleNamespace(
            template=SimpleNamespace(preview_image=None)
        )

        self.assertIsNone(
            self.serializer.get_template_preview_image(without_template)
        )
        self.assertIsNone(
            self.serializer.get_template_preview_image(without_preview_image)
        )


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
    def test_user_cannot_create_second_portfolio(self):
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
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            Portfolio.objects.filter(
                user=self.user
            ).count(),
            1
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

    def test_user_can_upload_project_image_while_preserving_legacy_url(self):
        legacy_image_url = 'https://example.com/project.png'

        with TemporaryDirectory() as media_root:
            with override_settings(MEDIA_ROOT=media_root):
                response = self.client.post(
                    f'/api/portfolios/{self.portfolio.id}/projects/',
                    {
                        'pro_name': 'Uploaded Project',
                        'pro_description': 'Project with an uploaded image',
                        'pro_image': legacy_image_url,
                        'pro_image_file': uploaded_project_image(
                            'uploaded-project.png'
                        ),
                        'pro_github_url': 'https://github.com/test/uploaded',
                        'pro_techs': 'Django',
                        'pro_live_demo_url': '',
                        'pro_start': '2026-01-01',
                        'pro_end': '',
                    },
                    format='multipart',
                )

                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                project = Project.objects.get(pro_name='Uploaded Project')
                project.refresh_from_db()
                self.assertEqual(project.pro_image, legacy_image_url)
                self.assertTrue(
                    Path(media_root, project.pro_image_file.name).is_file()
                )
                self.assertEqual(project.pro_end, None)

    def test_user_can_update_project_image_file(self):
        project = Project.objects.create(
            portfolio=self.portfolio,
            pro_name='Project to update',
            pro_description='Existing project',
            pro_image='https://example.com/legacy.png',
            pro_github_url='https://github.com/test/update',
            pro_techs='Django',
            pro_live_demo_url=None,
            pro_start='2026-01-01',
            pro_end='2026-02-01',
        )

        with TemporaryDirectory() as media_root:
            with override_settings(MEDIA_ROOT=media_root):
                response = self.client.patch(
                    f'/api/portfolios/{self.portfolio.id}/projects/{project.id}/',
                    {
                        'pro_image_file': uploaded_project_image(
                            'updated-project.png'
                        ),
                        'pro_end': '',
                    },
                    format='multipart',
                )

                self.assertEqual(response.status_code, status.HTTP_200_OK)
                project.refresh_from_db()
                self.assertEqual(project.pro_end, None)
                self.assertEqual(
                    project.pro_image,
                    'https://example.com/legacy.png',
                )
                self.assertTrue(
                    Path(media_root, project.pro_image_file.name).is_file()
                )

    def test_user_cannot_upload_project_to_another_users_portfolio(self):
        with TemporaryDirectory() as media_root:
            with override_settings(MEDIA_ROOT=media_root):
                response = self.client.post(
                    f'/api/portfolios/{self.other_portfolio.id}/projects/',
                    {
                        'pro_name': 'Unauthorized Upload',
                        'pro_github_url': 'https://github.com/test/unauthorized',
                        'pro_techs': 'Django',
                        'pro_start': '2026-01-01',
                        'pro_image_file': uploaded_project_image(
                            'unauthorized-project.png'
                        ),
                    },
                    format='multipart',
                )

                self.assertEqual(
                    response.status_code,
                    status.HTTP_404_NOT_FOUND,
                )
                self.assertFalse(
                    Project.objects.filter(
                        portfolio=self.other_portfolio,
                        pro_name='Unauthorized Upload',
                    ).exists()
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
class PortfolioValidationTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='validationuser',
            email='validation@example.com',
            password='TestPassword123!'
        )
        self.client.force_authenticate(user=self.user)

    def test_project_rejects_end_date_before_start_date(self):
        portfolio = Portfolio.objects.create(
            user=self.user,
            title='Test Portfolio',
            slug='validation-portfolio',
        )

        response = self.client.post(
            f'/api/portfolios/{portfolio.id}/projects/',
            {
                'pro_name': 'Test Project',
                'pro_description': 'Test description',
                'pro_image': None,
                'pro_github_url': 'https://github.com/test/project',
                'pro_techs': 'Django',
                'pro_live_demo_url': 'https://example.com',
                'pro_start': '2026-10-01',
                'pro_end': '2026-09-01',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn('pro_end', response.data)

    def test_project_accepts_valid_dates(self):
        portfolio = Portfolio.objects.create(
            user=self.user,
            title='Test Portfolio',
            slug='valid-project-portfolio',
        )

        response = self.client.post(
            f'/api/portfolios/{portfolio.id}/projects/',
            {
                'pro_name': 'Test Project',
                'pro_description': 'Test description',
                'pro_image': None,
                'pro_github_url': 'https://github.com/test/project',
                'pro_techs': 'Django',
                'pro_live_demo_url': 'https://example.com',
                'pro_start': '2026-01-01',
                'pro_end': '2026-10-01',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 201)

    def test_project_rejects_invalid_github_url(self):
        portfolio = Portfolio.objects.create(
            user=self.user,
            title='Test Portfolio',
            slug='invalid-github-portfolio',
        )

        response = self.client.post(
            f'/api/portfolios/{portfolio.id}/projects/',
            {
                'pro_name': 'Test Project',
                'pro_description': 'Test description',
                'pro_image': None,
                'pro_github_url': 'github.com/test/project',
                'pro_techs': 'Django',
                'pro_live_demo_url': 'https://example.com',
                'pro_start': '2026-01-01',
                'pro_end': None,
            },
            format='json',
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn('pro_github_url', response.data)

    def test_project_rejects_invalid_live_demo_url(self):
        portfolio = Portfolio.objects.create(
            user=self.user,
            title='Test Portfolio',
            slug='invalid-demo-portfolio',
        )

        response = self.client.post(
            f'/api/portfolios/{portfolio.id}/projects/',
            {
                'pro_name': 'Test Project',
                'pro_description': 'Test description',
                'pro_image': None,
                'pro_github_url': 'https://github.com/test/project',
                'pro_techs': 'Django',
                'pro_live_demo_url': 'example.com',
                'pro_start': '2026-01-01',
                'pro_end': None,
            },
            format='json',
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn('pro_live_demo_url', response.data)

    def test_skill_level_must_be_between_1_and_5(self):
        portfolio = Portfolio.objects.create(
            user=self.user,
            title='Test Portfolio',
            slug='skill-validation-portfolio',
        )

        for invalid_level in [0, 6, -1, 10]:
            response = self.client.post(
                f'/api/portfolios/{portfolio.id}/skills/',
                {
                    'skill_name': 'Django',
                    'skill_level_in_skill': invalid_level,
                },
                format='json',
            )

            self.assertEqual(response.status_code, 400)

    def test_skill_accepts_valid_level(self):
        portfolio = Portfolio.objects.create(
            user=self.user,
            title='Test Portfolio',
            slug='valid-skill-portfolio',
        )

        response = self.client.post(
            f'/api/portfolios/{portfolio.id}/skills/',
            {
                'skill_name': 'Django',
                'skill_level_in_skill': 5,
            },
            format='json',
        )

        self.assertEqual(response.status_code, 201)

    def test_experience_rejects_end_date_before_start_date(self):
        portfolio = Portfolio.objects.create(
            user=self.user,
            title='Test Portfolio',
            slug='experience-validation-portfolio',
        )

        response = self.client.post(
            f'/api/portfolios/{portfolio.id}/experiences/',
            {
                'ex_company': 'Test Company',
                'ex_start_date': '2026-10-01',
                'ex_end_date': '2026-09-01',
                'ex_position': 'Developer',
                'ex_description': 'Test experience',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn('ex_end_date', response.data)

    def test_experience_accepts_valid_dates(self):
        portfolio = Portfolio.objects.create(
            user=self.user,
            title='Test Portfolio',
            slug='valid-experience-portfolio',
        )

        response = self.client.post(
            f'/api/portfolios/{portfolio.id}/experiences/',
            {
                'ex_company': 'Test Company',
                'ex_start_date': '2026-01-01',
                'ex_end_date': '2026-10-01',
                'ex_position': 'Developer',
                'ex_description': 'Test experience',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 201)

    def test_social_links_reject_invalid_urls(self):
        portfolio = Portfolio.objects.create(
            user=self.user,
            title='Test Portfolio',
            slug='social-validation-portfolio',
        )

        response = self.client.post(
            f'/api/portfolios/{portfolio.id}/social-links/',
            {
                'sl_github': 'github.com/test',
                'sl_linkedin': 'linkedin.com/test',
                'sl_personal_web': 'example.com',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 400)

    def test_social_links_accept_valid_urls(self):
        portfolio = Portfolio.objects.create(
            user=self.user,
            title='Test Portfolio',
            slug='valid-social-portfolio',
        )

        response = self.client.post(
            f'/api/portfolios/{portfolio.id}/social-links/',
            {
                'sl_github': 'https://github.com/test',
                'sl_linkedin': 'https://linkedin.com/in/test',
                'sl_personal_web': 'https://example.com',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 201)

    def test_portfolio_rejects_empty_title(self):
        response = self.client.post(
            '/api/portfolios/',
            {
                'title': '   ',
                'slug': 'empty-title-portfolio',
                'bio': 'Test bio',
                'is_published': False,
            },
            format='json',
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn('title', response.data)

    def test_portfolio_strips_title_whitespace(self):
        response = self.client.post(
            '/api/portfolios/',
            {
                'title': '   My Portfolio   ',
                'slug': 'trimmed-title-portfolio',
                'bio': 'Test bio',
                'is_published': False,
            },
            format='json',
        )

        self.assertEqual(response.status_code, 201)

        portfolio = Portfolio.objects.get(
            slug='trimmed-title-portfolio'
        )

        self.assertEqual(portfolio.title, 'My Portfolio')

class PublicPortfolioSecurityTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='publicuser',
            email='public@example.com',
            password='TestPassword123!'
        )

        self.portfolio = Portfolio.objects.create(
            user=self.user,
            title='Public Portfolio',
            slug='public-portfolio',
            bio='Public bio',
            is_published=True,
        )

    def test_public_portfolio_does_not_expose_user_id(self):
        response = self.client.get(
            f'/api/portfolios/public/{self.portfolio.slug}/'
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotIn('user', response.data)

    def test_unpublished_portfolio_is_not_public(self):
        self.portfolio.is_published = False
        self.portfolio.save(update_fields=['is_published'])

        response = self.client.get(
            f'/api/portfolios/public/{self.portfolio.slug}/'
        )

        self.assertEqual(response.status_code, 404)
class PortfolioMassAssignmentSecurityTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='portfoliosecurity',
            email='portfoliosecurity@example.com',
            password='TestPassword123!'
        )

        self.other_user = User.objects.create_user(
            username='othersecurity',
            email='othersecurity@example.com',
            password='TestPassword123!'
        )

        self.portfolio = Portfolio.objects.create(
            user=self.user,
            title='Original Portfolio',
            slug='original-portfolio',
            is_published=False,
        )

        self.client.force_authenticate(user=self.user)

    def test_user_cannot_change_portfolio_owner(self):
        response = self.client.patch(
            f'/api/portfolios/{self.portfolio.id}/',
            {
                'user': self.other_user.id,
                'title': 'Updated Portfolio',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 200)

        self.portfolio.refresh_from_db()

        self.assertEqual(
            self.portfolio.user_id,
            self.user.id
        )

        self.assertEqual(
            self.portfolio.title,
            'Updated Portfolio'
        )

    def test_user_cannot_change_portfolio_id(self):
        original_id = self.portfolio.id

        response = self.client.patch(
            f'/api/portfolios/{self.portfolio.id}/',
            {
                'id': 999999,
                'title': 'Updated Portfolio',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 200)

        self.portfolio.refresh_from_db()

        self.assertEqual(
            self.portfolio.id,
            original_id
        )

    def test_portfolio_ignores_unknown_sensitive_fields(self):
        response = self.client.patch(
            f'/api/portfolios/{self.portfolio.id}/',
            {
                'password': 'hacked',
                'is_staff': True,
                'is_superuser': True,
                'title': 'Secure Portfolio',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 200)

        self.portfolio.refresh_from_db()

        self.assertEqual(
            self.portfolio.title,
            'Secure Portfolio'
        )

def test_portfolio_ignores_unknown_sensitive_fields(self):
    response = self.client.patch(
        f'/api/portfolios/{self.portfolio.id}/',
        {
            'password': 'hacked',
            'is_staff': True,
            'is_superuser': True,
            'title': 'Secure Portfolio',
        },
        format='json',
    )

    self.assertEqual(response.status_code, 200)

    self.portfolio.refresh_from_db()

    self.assertEqual(
        self.portfolio.title,
        'Secure Portfolio'
    )
    self.assertEqual(response.status_code, 400)


class ChildMassAssignmentSecurityTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='childsecurity',
            email='childsecurity@example.com',
            password='TestPassword123!'
        )

        self.other_user = User.objects.create_user(
            username='otherchildsecurity',
            email='otherchildsecurity@example.com',
            password='TestPassword123!'
        )

        self.portfolio = Portfolio.objects.create(
            user=self.user,
            title='Parent Portfolio',
            slug='parent-portfolio',
        )

        self.other_portfolio = Portfolio.objects.create(
            user=self.other_user,
            title='Other Portfolio',
            slug='other-parent-portfolio',
        )

        self.client.force_authenticate(user=self.user)

    def test_project_cannot_change_portfolio(self):
        response = self.client.post(
            f'/api/portfolios/{self.portfolio.id}/projects/',
            {
                'portfolio': self.other_portfolio.id,
                'pro_name': 'Secure Project',
                'pro_description': 'Test project',
                'pro_image': None,
                'pro_github_url': 'https://github.com/test/project',
                'pro_techs': 'Django',
                'pro_live_demo_url': None,
                'pro_start': '2026-01-01',
                'pro_end': None,
            },
            format='json',
        )

        self.assertEqual(response.status_code, 201)

        project = Project.objects.get(
            pro_name='Secure Project'
        )

        self.assertEqual(
            project.portfolio_id,
            self.portfolio.id
        )

def test_public_portfolio_exposes_safe_contact_information_only(self):
    self.user.job_title = 'Backend Developer'
    self.user.phone = '09123456789'
    self.user.location = 'Baku, Azerbaijan'
    self.user.save(
        update_fields=[
            'job_title',
            'phone',
            'location',
        ]
    )

    response = self.client.get(
        f'/api/portfolios/public/{self.portfolio.slug}/'
    )

    self.assertEqual(
        response.status_code,
        200
    )

    self.assertEqual(
        response.data['email'],
        'public@example.com'
    )

    self.assertEqual(
        response.data['job_title'],
        'Backend Developer'
    )

    self.assertEqual(
        response.data['location'],
        'Baku, Azerbaijan'
    )

    self.assertNotIn(
        'phone',
        response.data
    )

    self.assertNotIn(
        'user',
        response.data
    )

