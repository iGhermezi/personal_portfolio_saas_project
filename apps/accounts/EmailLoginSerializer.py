from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailLoginSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # جایگزین کردن فیلد username با email در ورودی
        self.fields['email'] = serializers.EmailField()

    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        # ۱. پیدا کردن کاربر بر اساس ایمیل
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"detail": "کاربری با این ایمیل پیدا نشد."})

        # ۲. بررسی درست بودن رمز عبور
        if not user.check_password(password):
            raise serializers.ValidationError({"detail": "رمز عبور اشتباه است."})
        
        if not user.is_active:
            raise serializers.ValidationError({"detail": "این حساب کاربری غیرفعال است."})

        # ۳. تولید توکن‌های JWT و خروجی
        refresh = self.get_token(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'email': user.email,
                'username': user.username,
            }
        }