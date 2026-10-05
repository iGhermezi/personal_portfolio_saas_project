from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.portfolios_themes.models import PortfolioTemplate
from django.conf import settings


class Portfolio(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="portfolio")
    template = models.ForeignKey(PortfolioTemplate,on_delete=models.SET_NULL,null=True,blank=True,related_name="portfolios")
    title =  models.CharField(max_length=100)
    slug = models.SlugField(max_length=255,unique=True)
    bio = models.TextField(null=True,blank=True)
    preview_image = models.ImageField(
    upload_to='portfolio_previews/',
    null=True,
    blank=True,
)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 


class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE,related_name="projects")
    pro_name = models.CharField(max_length=50)
    pro_description = models.TextField(null=True,blank=True)
    pro_image = models.TextField(null=True,blank=True)
    pro_image_file = models.ImageField(
    upload_to='projects/',
    null=True,
    blank=True,
)
    pro_github_url = models.TextField()
    pro_techs = models.TextField()
    pro_live_demo_url = models.TextField(null=True,blank=True)
    pro_start = models.DateField()
    pro_end = models.DateField(null=True,blank=True)

class Skill(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete = models.CASCADE,related_name="skills")
    skill_name = models.CharField(max_length=100)
    skill_level_in_skill = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])

class Education(models.Model):
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE,related_name="educations")
    edu = models.CharField(max_length=100)

class Experience(models.Model):
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE,related_name="experiences")
    ex_company = models.CharField(max_length=100)
    ex_start_date = models.DateField()
    ex_end_date = models.DateField(null=True,blank=True)
    ex_position = models.CharField(max_length=100)
    ex_description = models.TextField(null=True,blank=True)

class SocialLink(models.Model):
    portfolio = models.OneToOneField(Portfolio,on_delete=models.CASCADE,related_name="social")
    sl_github = models.TextField(null=True,blank=True)
    sl_linkedin = models.TextField(null=True,blank=True)
    sl_personal_web = models.TextField(null=True,blank=True)
