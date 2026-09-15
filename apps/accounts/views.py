from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .UserRegisterSerializer import UserRegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .EmailLoginSerializer import EmailLoginSerializer # نام فایلی که سریالایزر بالا توی اونه
from .UserProfileSerializer import UserProfileSerializer

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