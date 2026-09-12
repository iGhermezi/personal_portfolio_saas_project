from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_image_url = models.TextField(null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    location = models.TextField(null=True, blank=True)