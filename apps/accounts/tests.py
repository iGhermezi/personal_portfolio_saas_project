from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core import mail
from django.test import override_settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from rest_framework import status
from rest_framework.test import APITestCase

from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

@override_settings(
EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
)
class AccountsTests(APITestCase):

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

    # =========================================================
    # Register
    # =========================================================

    def test_user_can_register(self):
        data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'NewPassword123',
            'password2': 'NewPassword123',
        }

        response = self.client.post(
            '/api/accounts/register/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            User.objects.filter(
                email='new@example.com'
            ).exists()
        )

    def test_register_rejects_duplicate_email(self):
        data = {
            'username': 'anotheruser',
            'email': 'test@example.com',
            'password': 'NewPassword123',
            'password2': 'NewPassword123',
        }

        response = self.client.post(
            '/api/accounts/register/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            User.objects.filter(
                email='test@example.com'
            ).count(),
            1
        )

    def test_register_rejects_mismatched_passwords(self):
        data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'NewPassword123',
            'password2': 'DifferentPassword123',
        }

        response = self.client.post(
            '/api/accounts/register/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    # =========================================================
    # Login
    # =========================================================

    def test_user_can_login_with_email_and_password(self):
        data = {
            'email': 'test@example.com',
            'password': 'TestPassword123',
        }

        response = self.client.post(
            '/api/accounts/login/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertIn(
            'access',
            response.data
        )

        self.assertIn(
            'refresh',
            response.data
        )

        self.assertIn(
            'user',
            response.data
        )

        self.assertEqual(
            response.data['user']['email'],
            'test@example.com'
        )

    def test_login_rejects_wrong_password(self):
        data = {
            'email': 'test@example.com',
            'password': 'WrongPassword123',
        }

        response = self.client.post(
            '/api/accounts/login/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_login_rejects_unknown_email(self):
        data = {
            'email': 'unknown@example.com',
            'password': 'TestPassword123',
        }

        response = self.client.post(
            '/api/accounts/login/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    # =========================================================
    # JWT / Protected endpoint
    # =========================================================

    def test_profile_requires_authentication(self):
        response = self.client.get(
            '/api/accounts/me/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_authenticated_user_can_access_profile(self):
        self.client.force_authenticate(
            user=self.user
        )

        response = self.client.get(
            '/api/accounts/me/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['email'],
            'test@example.com'
        )

    def test_authenticated_user_can_update_profile(self):
        self.client.force_authenticate(
            user=self.user
        )

        data = {
            'username': 'updateduser',
            'first_name': 'Matin',
            'last_name': 'Test',
            'profile_image_url': 'https://example.com/image.jpg',
            'job_title': 'Backend Developer',
            'phone': '09123456789',
            'location': 'Tehran',
        }

        response = self.client.patch(
            '/api/accounts/me/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.user.refresh_from_db()

        self.assertEqual(
            self.user.username,
            'updateduser'
        )

        self.assertEqual(
            self.user.first_name,
            'Matin'
        )

        self.assertEqual(
            self.user.job_title,
            'Backend Developer'
        )

        self.assertEqual(
            self.user.location,
            'Tehran'
        )

    def test_profile_email_is_read_only(self):
        self.client.force_authenticate(
            user=self.user
        )

        data = {
            'email': 'hacker@example.com',
        }

        response = self.client.patch(
            '/api/accounts/me/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.user.refresh_from_db()

        self.assertEqual(
            self.user.email,
            'test@example.com'
        )

    # =========================================================
    # Logout
    # =========================================================

    def test_logout_blacklists_refresh_token(self):
        self.client.force_authenticate(
            user=self.user
        )

        refresh = RefreshToken.for_user(
            self.user
        )

        refresh_token = str(refresh)

        response = self.client.post(
            '/api/accounts/logout/',
            {
                'refresh': refresh_token
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_205_RESET_CONTENT
        )

        refresh_response = self.client.post(
            '/api/accounts/token/refresh/',
            {
                'refresh': refresh_token
            },
            format='json'
        )

        self.assertEqual(
            refresh_response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_logout_requires_refresh_token(self):
        self.client.force_authenticate(
            user=self.user
        )

        response = self.client.post(
            '/api/accounts/logout/',
            {},
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    # =========================================================
    # Email Change
    # =========================================================

    def test_user_can_request_email_change(self):
        self.client.force_authenticate(
            user=self.user
        )

        response = self.client.post(
            '/api/accounts/change-email/request/',
            {
                'new_email': 'newemail@example.com'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.user.refresh_from_db()

        self.assertEqual(
            self.user.pending_email,
            'newemail@example.com'
        )

        self.assertIsNotNone(
            self.user.email_change_code
        )

        self.assertEqual(
            len(self.user.email_change_code),
            6
        )

        self.assertEqual(
            len(mail.outbox),
            1
        )

        self.assertEqual(
            mail.outbox[0].to,
            ['newemail@example.com']
        )

    def test_email_change_confirm_changes_email(self):
        self.client.force_authenticate(
            user=self.user
        )

        request_response = self.client.post(
            '/api/accounts/change-email/request/',
            {
                'new_email': 'newemail@example.com'
            },
            format='json'
        )

        self.assertEqual(
            request_response.status_code,
            status.HTTP_200_OK
        )

        self.user.refresh_from_db()

        code = self.user.email_change_code

        confirm_response = self.client.post(
            '/api/accounts/change-email/confirm/',
            {
                'code': code
            },
            format='json'
        )

        self.assertEqual(
            confirm_response.status_code,
            status.HTTP_200_OK
        )

        self.user.refresh_from_db()

        self.assertEqual(
            self.user.email,
            'newemail@example.com'
        )

        self.assertIsNone(
            self.user.pending_email
        )

        self.assertIsNone(
            self.user.email_change_code
        )

        self.assertIsNone(
            self.user.email_change_code_created_at
        )

    def test_email_change_rejects_wrong_code(self):
        self.client.force_authenticate(
            user=self.user
        )

        self.client.post(
            '/api/accounts/change-email/request/',
            {
                'new_email': 'newemail@example.com'
            },
            format='json'
        )

        response = self.client.post(
            '/api/accounts/change-email/confirm/',
            {
                'code': '999999'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.user.refresh_from_db()

        self.assertEqual(
            self.user.email,
            'test@example.com'
        )

    def test_email_change_rejects_duplicate_email(self):
        self.client.force_authenticate(
            user=self.user
        )

        response = self.client.post(
            '/api/accounts/change-email/request/',
            {
                'new_email': 'other@example.com'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.user.refresh_from_db()

        self.assertIsNone(
            self.user.pending_email
        )

    # =========================================================
    # Forgot Password
    # =========================================================

    def test_forgot_password_sends_reset_email(self):
        response = self.client.post(
            '/api/accounts/password/forgot/',
            {
                'email': 'test@example.com'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(mail.outbox),
            1
        )

        self.assertEqual(
            mail.outbox[0].to,
            ['test@example.com']
        )

        self.assertIn(
            'reset-password',
            mail.outbox[0].body
        )

    def test_forgot_password_does_not_reveal_unknown_email(self):
        response = self.client.post(
            '/api/accounts/password/forgot/',
            {
                'email': 'unknown@example.com'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(mail.outbox),
            0
        )
        self.assertIn(
            'If an account with this email exists',
            response.data['detail']
        )

    # =========================================================
    # Password Reset
    # =========================================================

    def test_password_reset_changes_password(self):
        token_generator = PasswordResetTokenGenerator()

        uid = urlsafe_base64_encode(
            force_bytes(self.user.pk)
        )

        token = token_generator.make_token(
            self.user
        )

        response = self.client.post(
            '/api/accounts/password/reset/',
            {
                'uid': uid,
                'token': token,
                'new_password': 'NewPassword123',
                'confirm_password': 'NewPassword123',
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.user.refresh_from_db()

        self.assertTrue(
            self.user.check_password(
                'NewPassword123'
            )
        )

    def test_password_reset_rejects_mismatched_passwords(self):
        token_generator = PasswordResetTokenGenerator()

        uid = urlsafe_base64_encode(
            force_bytes(self.user.pk)
        )

        token = token_generator.make_token(
            self.user
        )

        response = self.client.post(
            '/api/accounts/password/reset/',
            {
                'uid': uid,
                'token': token,
                'new_password': 'NewPassword123',
                'confirm_password': 'DifferentPassword123',
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_password_reset_token_is_single_use(self):
        token_generator = PasswordResetTokenGenerator()

        uid = urlsafe_base64_encode(
            force_bytes(self.user.pk)
        )

        token = token_generator.make_token(
            self.user
        )

        first_response = self.client.post(
            '/api/accounts/password/reset/',
            {
                'uid': uid,
                'token': token,
                'new_password': 'NewPassword123',
                'confirm_password': 'NewPassword123',
            },
            format='json'
        )

        self.assertEqual(
            first_response.status_code,
            status.HTTP_200_OK
        )

        second_response = self.client.post(
            '/api/accounts/password/reset/',
            {
                'uid': uid,
                'token': token,
                'new_password': 'AnotherPassword123',
                'confirm_password': 'AnotherPassword123',
            },
            format='json'
        )

        self.assertEqual(
            second_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_password_reset_invalidates_old_refresh_token(self):
        refresh = RefreshToken.for_user(
            self.user
        )

        old_refresh_token = str(refresh)

        token_generator = PasswordResetTokenGenerator()

        uid = urlsafe_base64_encode(
            force_bytes(self.user.pk)
        )

        token = token_generator.make_token(
            self.user
        )

        response = self.client.post(
            '/api/accounts/password/reset/',
            {
                'uid': uid,
                'token': token,
                'new_password': 'NewPassword123',
                'confirm_password': 'NewPassword123',
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        refresh_response = self.client.post(
            '/api/accounts/token/refresh/',
            {
                'refresh': old_refresh_token
            },
            format='json'
        )

        self.assertEqual(
            refresh_response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_new_password_can_login_after_password_reset(self):
        token_generator = PasswordResetTokenGenerator()

        uid = urlsafe_base64_encode(
            force_bytes(self.user.pk)
        )

        token = token_generator.make_token(
            self.user
        )

        response = self.client.post(
            '/api/accounts/password/reset/',
            {
                'uid': uid,
                'token': token,
                'new_password': 'NewPassword123',
                'confirm_password': 'NewPassword123',
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        login_response = self.client.post(
            '/api/accounts/login/',
            {
                'email': 'test@example.com',
                'password': 'NewPassword123',
            },
            format='json'
        )

        self.assertEqual(
            login_response.status_code,
            status.HTTP_200_OK
        )

        self.assertIn(
            'access',
            login_response.data
        )

        self.assertIn(
            'refresh',
            login_response.data
        )

    def test_old_password_cannot_login_after_password_reset(self):
        token_generator = PasswordResetTokenGenerator()

        uid = urlsafe_base64_encode(
            force_bytes(self.user.pk)
        )

        token = token_generator.make_token(
            self.user
        )

        response = self.client.post(
            '/api/accounts/password/reset/',
            {
                'uid': uid,
                'token': token,
                'new_password': 'NewPassword123',
                'confirm_password': 'NewPassword123',
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        login_response = self.client.post(
            '/api/accounts/login/',
            {
                'email': 'test@example.com',
                'password': 'TestPassword123',
            },
            format='json'
        )

        self.assertEqual(
            login_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
