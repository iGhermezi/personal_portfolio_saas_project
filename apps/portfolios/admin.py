from django.contrib import admin
from .models import Portfolio, Experience, Education, Project, Skill, SocialLink

admin.site.register(Portfolio)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(SocialLink)