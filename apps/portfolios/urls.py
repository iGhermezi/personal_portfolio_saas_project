from django.urls import path

from .views import (
    PortfolioListCreateView,
    PortfolioDetailView,
    PublicPortfolioDetailView,
    ProjectListCreateView,
    ProjectDetailView,
    SkillListCreateView,
    SkillDetailView,
    EducationListCreateView,
    EducationDetailView,
    ExperienceListCreateView,
    ExperienceDetailView,
    SocialLinkCreateView,
    SocialLinkDetailView,
)


urlpatterns = [
    # اندپوینت‌های پورتفولیو
    path(
        '',
        PortfolioListCreateView.as_view(),
        name='portfolio_list_create'
    ),

    path(
        '<int:pk>/',
        PortfolioDetailView.as_view(),
        name='portfolio_detail'
    ),

    path(
        'public/<slug:slug>/',
        PublicPortfolioDetailView.as_view(),
        name='public_portfolio_detail'
    ),


    # اندپوینت‌های پروژه‌ها
    path(
        '<int:portfolio_pk>/projects/',
        ProjectListCreateView.as_view(),
        name='project_list_create'
    ),

    path(
        '<int:portfolio_pk>/projects/<int:pk>/',
        ProjectDetailView.as_view(),
        name='project_detail'
    ),


    # اندپوینت‌های مهارت‌ها
    path(
        '<int:portfolio_pk>/skills/',
        SkillListCreateView.as_view(),
        name='skill_list_create'
    ),

    path(
        '<int:portfolio_pk>/skills/<int:pk>/',
        SkillDetailView.as_view(),
        name='skill_detail'
    ),


    # اندپوینت‌های تحصیلات
    path(
        '<int:portfolio_pk>/educations/',
        EducationListCreateView.as_view(),
        name='education_list_create'
    ),

    path(
        '<int:portfolio_pk>/educations/<int:pk>/',
        EducationDetailView.as_view(),
        name='education_detail'
    ),


    # اندپوینت‌های سوابق کاری
    path(
        '<int:portfolio_pk>/experiences/',
        ExperienceListCreateView.as_view(),
        name='experience_list_create'
    ),

    path(
        '<int:portfolio_pk>/experiences/<int:pk>/',
        ExperienceDetailView.as_view(),
        name='experience_detail'
    ),

    # اندپوینت‌های لینک‌های اجتماعی
    path(
        '<int:portfolio_pk>/social-links/',
        SocialLinkCreateView.as_view(),
        name='social-link_create'
    ),

    path(
        '<int:portfolio_pk>/social-links/<int:pk>/',
        SocialLinkDetailView.as_view(),
        name='social-link_detail'
    ),
]