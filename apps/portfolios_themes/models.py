from django.db import models

class PortfolioTemplate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preview_img = models.TextField()
    
    # اضافه کردن default برای حل مشکل مایگریشن
    template_key = models.CharField(max_length=50, unique=True, null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {'(Premium)' if self.is_premium else '(Free)'}"