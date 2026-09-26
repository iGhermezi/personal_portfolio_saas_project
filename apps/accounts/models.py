from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q


class User(AbstractUser):
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    has_active_subscription = models.BooleanField(default=False)

    profile_image_url = models.TextField(null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    location = models.TextField(null=True, blank=True)

    pending_email = models.EmailField(null=True, blank=True)
    email_change_code = models.CharField(max_length=6, null=True, blank=True)
    email_change_code_created_at = models.DateTimeField(
        null=True,
        blank=True
    )


class PremiumRequest(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_APPROVED, 'Approved'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='premium_requests',
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    reviewed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reviewed_premium_requests',
    )

    class Meta:
        ordering = ('-created_at',)
        constraints = [
            models.UniqueConstraint(
                fields=('user',),
                condition=Q(status='pending'),
                name='unique_pending_premium_request_per_user',
            ),
        ]

    def __str__(self):
        return f'{self.user.email} - {self.status}'