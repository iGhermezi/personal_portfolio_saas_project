from django.urls import path

from .views import PortfolioTemplateListView


urlpatterns = [
    path(
        '',
        PortfolioTemplateListView.as_view(),
        name='template_list'
    ),
]