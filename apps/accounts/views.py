import secrets
import string
from datetime import timedelta
from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken,
    BlacklistedToken,
)

from .user_register_serializer import UserRegisterSerializer
from .email_login_serializer import EmailLoginSerializer
from .user_profile_serializer import UserProfileSerializer

from .email_change_serializer import (
    EmailChangeRequestSerializer,
    EmailChangeConfirmSerializer,
)

from .password_forgot_serializer import PasswordForgotSerializer
from .password_reset_serializer import PasswordResetSerializer

from .email_verification_serializer import (
    EmailVerificationSerializer,
)

from .email_verification_resend_serializer import (
    EmailVerificationResendSerializer,
)
from .change_password_serializer import ChangePasswordSerializer

from .throttles import (
    AuthRateThrottle,
    SensitiveActionThrottle,
)
from .models import PremiumRequest

User = get_user_model()

class PremiumRequestView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        premium_request = (
            PremiumRequest.objects
            .filter(user=request.user)
            .first()
        )

        return Response({
            'has_subscription': request.user.has_active_subscription,
            'request_status': (
                premium_request.status
                if premium_request
                else None
            ),
        })

    def post(self, request):
        if request.user.has_active_subscription:
            return Response(
                {
                    'detail': (
                        'Your account already has '
                        'Premium access.'
                    )
                },
                status=400,
            )

        premium_request = (
            PremiumRequest.objects
            .filter(
                user=request.user,
                status=PremiumRequest.STATUS_PENDING,
            )
            .first()
        )

        if premium_request:
            return Response(
                {
                    'detail': (
                        'Your Premium request is already '
                        'pending.'
                    ),
                    'status': premium_request.status,
                },
                status=200,
            )

        premium_request = PremiumRequest.objects.create(
            user=request.user,
        )

        send_mail(
            subject='New Premium Upgrade Request',
            message=(
                'A new Premium upgrade request has been '
                'submitted.\n\n'
                f'Username: {request.user.username}\n'
                f'Email: {request.user.email}\n'
                f'Request ID: {premium_request.id}\n\n'
                'Please review this request in Django Admin.'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[
                settings.SUPPORT_EMAIL,
            ],
        )

        return Response(
            {
                'detail': (
                    'Your Premium request has been submitted.'
                ),
                'status': premium_request.status,
            },
            status=201,
        )

def invalidate_user_sessions(user):
    outstanding_tokens = OutstandingToken.objects.filter(user=user)

    for outstanding_token in outstanding_tokens:
        BlacklistedToken.objects.get_or_create(token=outstanding_token)


def send_email_verification_email(user):
    token_generator = PasswordResetTokenGenerator()

    uid = urlsafe_base64_encode(
        force_bytes(user.pk)
    )

    token = token_generator.make_token(
        user
    )

    verification_url = (
        f'http://localhost:8000/api/accounts/'
        f'email/verify/{uid}/{token}/'
    )

    send_mail(
        subject='Verify your email',
        message=(
            'Please verify your email address by opening '
            'the link below:\n\n'
            f'{verification_url}\n\n'
            'If you did not create this account, '
            'please ignore this email.'
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer
    throttle_classes = (AuthRateThrottle,)

    def perform_create(self, serializer):
        user = serializer.save()

        send_email_verification_email(
            user
        )

class LoginView(TokenObtainPairView):
    serializer_class = EmailLoginSerializer
    throttle_classes = (AuthRateThrottle,)


class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_object(self):
        return self.request.user


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)
    throttle_classes = (SensitiveActionThrottle,)

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)

        user = request.user
        new_password = serializer.validated_data['new_password']

        user.set_password(new_password)
        user.save(update_fields=['password'])

        invalidate_user_sessions(user)

        return Response({
            'detail': (
                'Password changed successfully. '
                'All sessions have been invalidated.'
            )
        })

class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        refresh_token = request.data.get(
            'refresh'
        )

        if not refresh_token:
            return Response(
                {
                    'detail': 'refresh token is required'
                },
                status=400
            )

        try:
            token = RefreshToken(
                refresh_token
            )

            token.blacklist()

        except TokenError:
            return Response(
                {
                    'detail': (
                        'token is invalid or has already '
                        'been invalidated'
                    )
                },
                status=400
            )

        return Response(
            {
                'detail': 'logout successful'
            },
            status=205
        )


class EmailChangeRequestView(generics.GenericAPIView):
    serializer_class = EmailChangeRequestSerializer
    permission_classes = (permissions.IsAuthenticated,)
    throttle_classes = (SensitiveActionThrottle,)

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        new_email = serializer.validated_data[
            'new_email'
        ]

        code = ''.join(
            secrets.choice(string.digits)
            for _ in range(6)
        )

        user = request.user

        user.pending_email = new_email
        user.email_change_code = code
        user.email_change_code_created_at = (
            timezone.now()
        )

        user.save()

        send_mail(
            subject="code for changing email",
            message=(
                f'your verification code: {code}\n'
                'this code is valid for 10 minutes.'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[new_email],
        )

        return Response({
            'detail': (
                'verification code sent to your new email.'
            )
        })


class EmailChangeConfirmView(generics.GenericAPIView):
    serializer_class = EmailChangeConfirmSerializer
    permission_classes = (permissions.IsAuthenticated,)
    throttle_classes = (SensitiveActionThrottle,)

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        code = serializer.validated_data[
            'code'
        ]

        user = request.user

        if (
            not user.pending_email
            or not user.email_change_code
        ):
            return Response(
                {
                    'detail': (
                        'no email change request found.'
                    )
                },
                status=400
            )

        if user.email_change_code != code:
            return Response(
                {
                    'detail': (
                        'incorrect verification code.'
                    )
                },
                status=400
            )

        expires_at = (
            user.email_change_code_created_at
            + timedelta(minutes=10)
        )

        if timezone.now() > expires_at:
            return Response(
                {
                    'detail': (
                        'verification code has expired.'
                    )
                },
                status=400
            )

        user.email = user.pending_email

        user.pending_email = None
        user.email_change_code = None
        user.email_change_code_created_at = None

        # ایمیل جدید هنوز تأیید نشده است.
        user.email_verified = False

        user.save()

        # ارسال لینک تأیید به ایمیل جدید
        send_email_verification_email(
            user
        )

        return Response({
            'detail': (
                'email changed successfully. '
                'please verify your new email address.'
            )
        })

class EmailVerificationView(generics.GenericAPIView):
    serializer_class = EmailVerificationSerializer
    permission_classes = (permissions.AllowAny,)
    throttle_classes = (AuthRateThrottle,)

    def get(self, request, uid, token):
        serializer = self.get_serializer(
            data={
                'uid': uid,
                'token': token,
            }
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = serializer.validated_data[
            'user'
        ]

        user.email_verified = True
        user.save(
            update_fields=[
                'email_verified'
            ]
        )

        return HttpResponse(
            'Email verified successfully.',
            status=200,
            content_type='text/plain',
        )

class EmailVerificationResendView(generics.GenericAPIView):
    serializer_class = EmailVerificationResendSerializer
    permission_classes = (permissions.AllowAny,)
    throttle_classes = (AuthRateThrottle,)

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        email = serializer.validated_data[
            'email'
        ]

        user = User.objects.filter(
            email__iexact=email
        ).first()

        if user and not user.email_verified:
            send_email_verification_email(
                user
            )

        return Response({
            'detail': (
                'If an account with this email exists '
                'and is not verified, a verification email '
                'will be sent.'
            )
        })


class PasswordForgotView(generics.GenericAPIView):
    serializer_class = PasswordForgotSerializer
    permission_classes = (permissions.AllowAny,)
    throttle_classes = (AuthRateThrottle,)

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        email = serializer.validated_data[
            'email'
        ]

        user = User.objects.filter(
            email__iexact=email
        ).first()

        if user:
            token_generator = PasswordResetTokenGenerator()

            uid = urlsafe_base64_encode(
                force_bytes(user.pk)
            )

            token = token_generator.make_token(
                user
            )

            reset_url = (
                f'http://localhost:5173/reset-password/'
                f'{uid}/{token}/'
            )

            send_mail(
                subject="Password Reset",
                message=(
                    "To set a new password, please use "
                    "the link below:\n\n"
                    f"{reset_url}\n\n"
                    "If you did not request this, "
                    "please ignore this email."
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )

        return Response({
            'detail': (
                'If an account with this email exists, '
                'the password reset link will be sent.'
            )
        })


class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = (permissions.AllowAny,)
    throttle_classes = (AuthRateThrottle,)

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = serializer.validated_data[
            'user'
        ]

        new_password = serializer.validated_data[
            'new_password'
        ]

        user.set_password(
            new_password
        )

        user.save()

        invalidate_user_sessions(user)

        return Response({
            'detail': (
                'password has been reset successfully '
                'and all sessions have been invalidated.'
            )
        })