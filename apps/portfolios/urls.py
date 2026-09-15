from django.urls import path
from .views import (
    PortfolioListCreateView,
    PortfolioDetailView,
    PublicPortfolioDetailView,
    ProjectListCreateView,
    ProjectDetailView,
    SkillListCreateView,
    SkillDetailView,
)

urlpatterns = [
    # اندپوینت‌های پورتفولیو
    path('', PortfolioListCreateView.as_view(), name='portfolio_list_create'),
    path('<int:pk>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('public/<slug:slug>/', PublicPortfolioDetailView.as_view(), name='public_portfolio_detail'),

    # اندپوینت‌های پروژه‌ها (تودرتو، زیر یک پورتفولیوی مشخص)
    path('<int:portfolio_pk>/projects/', ProjectListCreateView.as_view(), name='project_list_create'),
    path('<int:portfolio_pk>/projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),

    # اندپوینت‌های مهارت‌ها (تودرتو، زیر یک پورتفولیوی مشخص)
    path('<int:portfolio_pk>/skills/', SkillListCreateView.as_view(), name='skill_list_create'),
    path('<int:portfolio_pk>/skills/<int:pk>/', SkillDetailView.as_view(), name='skill_detail'),
]