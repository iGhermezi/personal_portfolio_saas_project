from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    
    profile_image_url = models.TextField(null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    location = models.TextField(null=True, blank=True)

    pending_email = models.EmailField(null=True, blank=True)
    email_change_code = models.CharField(max_length=6, null=True, blank=True)
    email_change_code_created_at = models.DateTimeField(null=True, blank=True)