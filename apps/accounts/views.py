import random
import string
from datetime import timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils import timezone

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from .UserRegisterSerializer import UserRegisterSerializer
from .EmailLoginSerializer import EmailLoginSerializer
from .UserProfileSerializer import UserProfileSerializer
from .EmailChangeSerializer import EmailChangeRequestSerializer, EmailChangeConfirmSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer


class LoginView(TokenObtainPairView):
    serializer_class = EmailLoginSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_object(self):
        # کاربر فعلی که توکن JWT معتبر فرستاده را برمی‌گرداند
        return self.request.user


class LogoutView(APIView):
    """
    کاربر توکن refresh خودش رو می‌فرسته، ما اون رو باطل (blacklist) می‌کنیم
    تا حتی اگه هنوز منقضی نشده باشه، دیگه قابل استفاده نباشه.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        refresh_token = request.data.get('refresh')

        if not refresh_token:
            return Response({'detail': 'فیلد refresh لازم است.'}, status=400)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except TokenError:
            return Response({'detail': 'توکن نامعتبر یا از قبل باطل‌شده است.'}, status=400)

        return Response({'detail': 'خروج با موفقیت انجام شد.'}, status=205)


class EmailChangeRequestView(generics.GenericAPIView):
    """
    مرحله‌ی اول تغییر ایمیل: کاربر ایمیل جدید را می‌فرستد،
    یک کد ۶ رقمی ساخته می‌شود و به همان ایمیل جدید ارسال می‌شود.
    """
    serializer_class = EmailChangeRequestSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_email = serializer.validated_data['new_email']

        code = ''.join(random.choices(string.digits, k=6))

        user = request.user
        user.pending_email = new_email
        user.email_change_code = code
        user.email_change_code_created_at = timezone.now()
        user.save()

        send_mail(
            subject='کد تایید تغییر ایمیل',
            message=f'کد تایید شما: {code}\nاین کد تا ۱۰ دقیقه معتبر است.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[new_email],
        )

        return Response({'detail': 'کد تایید به ایمیل جدید ارسال شد.'})


class EmailChangeConfirmView(generics.GenericAPIView):
    """
    مرحله‌ی دوم: کاربر کد دریافتی را می‌فرستد؛
    اگر درست و هنوز معتبر بود، ایمیل واقعاً عوض می‌شود.
    """
    serializer_class = EmailChangeConfirmSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']

        user = request.user

        if not user.pending_email or not user.email_change_code:
            return Response(
                {'detail': 'درخواستی برای تغییر ایمیل ثبت نشده است.'},
                status=400
            )

        if user.email_change_code != code:
            return Response({'detail': 'کد وارد شده اشتباه است.'}, status=400)

        expires_at = user.email_change_code_created_at + timedelta(minutes=10)
        if timezone.now() > expires_at:
            return Response({'detail': 'کد منقضی شده، دوباره درخواست بدهید.'}, status=400)

        user.email = user.pending_email
        user.pending_email = None
        user.email_change_code = None
        user.email_change_code_created_at = None
        user.save()

        return Response({'detail': 'ایمیل با موفقیت تغییر کرد.'})