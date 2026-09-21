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

        self.user.email_verified = True
        self.user.save()

        self.other_user = User.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='TestPassword123'
        )

        self.other_user.email_verified = True
        self.other_user.save()

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

            user = User.objects.get(
                email='new@example.com'
            )

            self.assertFalse(
                user.email_verified
            )

            self.assertEqual(
                len(mail.outbox),
                1
            )

            self.assertEqual(
                mail.outbox[0].to,
                ['new@example.com']
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
    # Email Verification
    # =========================================================

    def test_register_creates_unverified_user(self):
        data = {
            'username': 'verificationuser',
            'email': 'verification@example.com',
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

        user = User.objects.get(
            email='verification@example.com'
        )

        self.assertFalse(
            user.email_verified
        )

    def test_register_sends_verification_email(self):
        data = {
            'username': 'verificationuser',
            'email': 'verification@example.com',
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

        self.assertEqual(
            len(mail.outbox),
            1
        )

        self.assertEqual(
            mail.outbox[0].to,
            ['verification@example.com']
        )

        self.assertIn(
            '/api/accounts/email/verify/',
            mail.outbox[0].body
        )

    def test_unverified_user_cannot_login(self):
        user = User.objects.create_user(
            username='unverifieduser',
            email='unverified@example.com',
            password='TestPassword123'
        )

        self.assertFalse(
            user.email_verified
        )

        response = self.client.post(
            '/api/accounts/login/',
            {
                'email': 'unverified@example.com',
                'password': 'TestPassword123',
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertIn(
            'not verified',
            str(response.data).lower()
        )

    def test_user_can_verify_email(self):
        user = User.objects.create_user(
            username='verifyuser',
            email='verify@example.com',
            password='TestPassword123'
        )

        token_generator = PasswordResetTokenGenerator()

        uid = urlsafe_base64_encode(
            force_bytes(user.pk)
        )

        token = token_generator.make_token(
            user
        )

        response = self.client.get(
            f'/api/accounts/email/verify/{uid}/{token}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        user.refresh_from_db()

        self.assertTrue(
            user.email_verified
        )

    def test_verified_user_can_login(self):
        user = User.objects.create_user(
            username='verifieduser',
            email='verified@example.com',
            password='TestPassword123'
        )

        user.email_verified = True
        user.save()

        response = self.client.post(
            '/api/accounts/login/',
            {
                'email': 'verified@example.com',
                'password': 'TestPassword123',
            },
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

    def test_email_verification_token_cannot_be_used_twice(self):
        user = User.objects.create_user(
            username='verifytwice',
            email='verifytwice@example.com',
            password='TestPassword123'
        )

        token_generator = PasswordResetTokenGenerator()

        uid = urlsafe_base64_encode(
            force_bytes(user.pk)
        )

        token = token_generator.make_token(
            user
        )

        first_response = self.client.get(
            f'/api/accounts/email/verify/{uid}/{token}/'
        )

        self.assertEqual(
            first_response.status_code,
            status.HTTP_200_OK
        )

        second_response = self.client.get(
            f'/api/accounts/email/verify/{uid}/{token}/'
        )

        self.assertEqual(
            second_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_invalid_email_verification_token_is_rejected(self):
        user = User.objects.create_user(
            username='invalidtoken',
            email='invalidtoken@example.com',
            password='TestPassword123'
        )

        uid = urlsafe_base64_encode(
            force_bytes(user.pk)
        )

        response = self.client.get(
            f'/api/accounts/email/verify/{uid}/invalid-token/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        user.refresh_from_db()

        self.assertFalse(
            user.email_verified
        )

    def test_email_verification_with_other_users_token_is_rejected(self):
        first_user = User.objects.create_user(
            username='firstverify',
            email='firstverify@example.com',
            password='TestPassword123'
        )

        second_user = User.objects.create_user(
            username='secondverify',
            email='secondverify@example.com',
            password='TestPassword123'
        )

        token_generator = PasswordResetTokenGenerator()

        first_uid = urlsafe_base64_encode(
            force_bytes(first_user.pk)
        )

        second_token = token_generator.make_token(
            second_user
        )

        response = self.client.get(
            f'/api/accounts/email/verify/'
            f'{first_uid}/{second_token}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        first_user.refresh_from_db()
        second_user.refresh_from_db()

        self.assertFalse(
            first_user.email_verified
        )

        self.assertFalse(
            second_user.email_verified
        )

    def test_resend_verification_email(self):
        user = User.objects.create_user(
            username='resenduser',
            email='resend@example.com',
            password='TestPassword123'
        )

        response = self.client.post(
            '/api/accounts/email/verification/resend/',
            {
                'email': 'resend@example.com'
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
            ['resend@example.com']
        )

        self.assertIn(
            '/api/accounts/email/verify/',
            mail.outbox[0].body
        )

    def test_resend_verification_does_not_reveal_unknown_email(self):
        response = self.client.post(
            '/api/accounts/email/verification/resend/',
            {
                'email': 'unknown-verification@example.com'
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

    def test_resend_verification_for_already_verified_user_does_not_send_email(self):
        user = User.objects.create_user(
            username='alreadyverified',
            email='alreadyverified@example.com',
            password='TestPassword123'
        )

        user.email_verified = True
        user.save()

        response = self.client.post(
            '/api/accounts/email/verification/resend/',
            {
                'email': 'alreadyverified@example.com'
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

    def test_email_change_requires_new_email_verification(self):
        self.client.force_authenticate(
            user=self.user
        )

        request_response = self.client.post(
            '/api/accounts/change-email/request/',
            {
                'new_email': 'changed@example.com'
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
            'changed@example.com'
        )

        self.assertFalse(
            self.user.email_verified
        )

        self.assertEqual(
            len(mail.outbox),
            2
        )

        self.assertIn(
            '/api/accounts/email/verify/',
            mail.outbox[1].body
        )

    def test_changed_email_cannot_login_before_verification(self):
        self.client.force_authenticate(
            user=self.user
        )

        request_response = self.client.post(
            '/api/accounts/change-email/request/',
            {
                'new_email': 'changed-login@example.com'
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

        self.assertFalse(
            self.user.email_verified
        )

        self.client.force_authenticate(
            user=None
        )

        login_response = self.client.post(
            '/api/accounts/login/',
            {
                'email': 'changed-login@example.com',
                'password': 'TestPassword123',
            },
            format='json'
        )

        self.assertEqual(
            login_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertIn(
            'not verified',
            str(login_response.data).lower()
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
class ChangePasswordTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='changepassuser',
            email='changepass@example.com',
            password='OldPassword123!',
            email_verified=True,
        )

        login_response = self.client.post(
            '/api/accounts/login/',
            {
                'email': 'changepass@example.com',
                'password': 'OldPassword123!',
            },
            format='json',
        )

        self.access_token = login_response.data['access']
        self.refresh_token = login_response.data['refresh']

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

    def test_change_password_success(self):
        response = self.client.post(
            '/api/accounts/change-password/',
            {
                'current_password': 'OldPassword123!',
                'new_password': 'NewPassword123!',
                'confirm_password': 'NewPassword123!',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 200)

        self.user.refresh_from_db()

        self.assertTrue(
            self.user.check_password('NewPassword123!')
        )

    def test_change_password_wrong_current_password(self):
        response = self.client.post(
            '/api/accounts/change-password/',
            {
                'current_password': 'WrongPassword123!',
                'new_password': 'NewPassword123!',
                'confirm_password': 'NewPassword123!',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 400)

        self.user.refresh_from_db()

        self.assertTrue(
            self.user.check_password('OldPassword123!')
        )

    def test_change_password_mismatched_passwords(self):
        response = self.client.post(
            '/api/accounts/change-password/',
            {
                'current_password': 'OldPassword123!',
                'new_password': 'NewPassword123!',
                'confirm_password': 'DifferentPassword123!',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 400)

        self.user.refresh_from_db()

        self.assertTrue(
            self.user.check_password('OldPassword123!')
        )

    def test_change_password_cannot_use_same_password(self):
        response = self.client.post(
            '/api/accounts/change-password/',
            {
                'current_password': 'OldPassword123!',
                'new_password': 'OldPassword123!',
                'confirm_password': 'OldPassword123!',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 400)

    def test_change_password_requires_authentication(self):
        self.client.credentials()

        response = self.client.post(
            '/api/accounts/change-password/',
            {
                'current_password': 'OldPassword123!',
                'new_password': 'NewPassword123!',
                'confirm_password': 'NewPassword123!',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 401)

    def test_change_password_invalidates_refresh_token(self):
        response = self.client.post(
            '/api/accounts/change-password/',
            {
                'current_password': 'OldPassword123!',
                'new_password': 'NewPassword123!',
                'confirm_password': 'NewPassword123!',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 200)

        refresh_response = self.client.post(
            '/api/accounts/token/refresh/',
            {
                'refresh': self.refresh_token,
            },
            format='json',
        )

        self.assertEqual(refresh_response.status_code, 401)


class UserProfileSecurityTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='profileuser',
            email='profile@example.com',
            password='ProfilePassword123!',
            email_verified=True,
        )

        login_response = self.client.post(
            '/api/accounts/login/',
            {
                'email': 'profile@example.com',
                'password': 'ProfilePassword123!',
            },
            format='json',
        )

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {login_response.data['access']}"
        )

    def test_user_can_update_allowed_profile_fields(self):
        response = self.client.patch(
            '/api/accounts/me/',
            {
                'username': 'newusername',
                'job_title': 'Backend Developer',
                'phone': '09123456789',
                'location': 'Tehran',
                'profile_image_url': 'https://example.com/avatar.jpg',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 200)

        self.user.refresh_from_db()

        self.assertEqual(self.user.username, 'newusername')
        self.assertEqual(self.user.job_title, 'Backend Developer')
        self.assertEqual(self.user.phone, '09123456789')
        self.assertEqual(self.user.location, 'Tehran')
        self.assertEqual(
            self.user.profile_image_url,
            'https://example.com/avatar.jpg'
        )

    def test_user_cannot_modify_sensitive_fields(self):
        response = self.client.patch(
            '/api/accounts/me/',
            {
                'is_staff': True,
                'is_superuser': True,
                'is_active': False,
                'email_verified': True,
                'email': 'hacker@example.com',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 200)

        self.user.refresh_from_db()

        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.user.email_verified)
        self.assertEqual(
            self.user.email,
            'profile@example.com'
        )

    def test_profile_does_not_expose_sensitive_fields(self):
        response = self.client.get(
            '/api/accounts/me/'
        )

        self.assertEqual(response.status_code, 200)

        self.assertNotIn('password', response.data)
        self.assertNotIn('is_staff', response.data)
        self.assertNotIn('is_superuser', response.data)
        self.assertNotIn('email_verified', response.data)
        self.assertNotIn('pending_email', response.data)
        self.assertNotIn('email_change_code', response.data)


class UserProfileSecurityTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='securityuser',
            email='security@example.com',
            password='TestPassword123!'
        )
        self.client.force_authenticate(user=self.user)

    def test_allowed_profile_fields_can_be_updated(self):
        response = self.client.patch(
            '/api/accounts/me/',
            {
                'username': 'updated_username',
                'job_title': 'Backend Developer',
                'phone': '09123456789',
                'location': 'Tehran',
                'profile_image_url': 'https://example.com/profile.jpg',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 200)

        self.user.refresh_from_db()

        self.assertEqual(
            self.user.username,
            'updated_username'
        )
        self.assertEqual(
            self.user.job_title,
            'Backend Developer'
        )
        self.assertEqual(
            self.user.phone,
            '09123456789'
        )
        self.assertEqual(
            self.user.location,
            'Tehran'
        )

    def test_sensitive_profile_fields_cannot_be_modified(self):
        original_email = self.user.email

        response = self.client.patch(
            '/api/accounts/me/',
            {
                'email': 'attacker@example.com',
                'email_verified': True,
                'is_staff': True,
                'is_superuser': True,
            },
            format='json',
        )

        self.assertEqual(response.status_code, 200)

        self.user.refresh_from_db()

        self.assertEqual(
            self.user.email,
            original_email
        )
        self.assertFalse(
            self.user.email_verified
        )
        self.assertFalse(
            self.user.is_staff
        )
        self.assertFalse(
            self.user.is_superuser
        )

    def test_sensitive_profile_fields_are_not_exposed(self):
        response = self.client.get(
            '/api/accounts/me/'
        )

        self.assertEqual(response.status_code, 200)

        self.assertNotIn(
            'password',
            response.data
        )
        self.assertNotIn(
            'email_verified',
            response.data
        )
        self.assertNotIn(
            'is_staff',
            response.data
        )
        self.assertNotIn(
            'is_superuser',
            response.data
        )
        self.assertNotIn(
            'pending_email',
            response.data
        )
        self.assertNotIn(
            'email_change_code',
            response.data
        )