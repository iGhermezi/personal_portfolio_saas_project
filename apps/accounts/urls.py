from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    UserProfileView,
    EmailChangeRequestView,
    EmailChangeConfirmView,
    PasswordForgotView,
    PasswordResetView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', LoginView.as_view(), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', UserProfileView.as_view(), name='user_profile'),
    path('change-email/request/', EmailChangeRequestView.as_view(), name='change_email_request'),
    path('change-email/confirm/', EmailChangeConfirmView.as_view(), name='change_email_confirm'),
    path('password/forgot/',PasswordForgotView.as_view(),name='password_forgot'),
    path('password/reset/',PasswordResetView.as_view(),name='password_reset'),
]