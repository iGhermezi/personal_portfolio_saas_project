from django.db import models


class PortfolioTemplate(models.Model):

    ACCESS_FREE = 'free'
    ACCESS_VERIFIED = 'verified'
    ACCESS_PREMIUM = 'premium'

    ACCESS_LEVELS = [
        (ACCESS_FREE, 'Free'),
        (ACCESS_VERIFIED, 'Verified Email'),
        (ACCESS_PREMIUM, 'Premium'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    preview_img = models.TextField()
    preview_image = models.ImageField(
    upload_to='template_previews/',
    null=True,
    blank=True,
)

    template_key = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True
    )

    access_level = models.CharField(
        max_length=20,
        choices=ACCESS_LEVELS,
        default=ACCESS_FREE
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name