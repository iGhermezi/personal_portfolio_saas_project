from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('apps.accounts.urls')),
    path('api/themes/', include('apps.portfolios_themes.urls')),
    path('api/portfolios/', include('apps.portfolios.urls')),
]
