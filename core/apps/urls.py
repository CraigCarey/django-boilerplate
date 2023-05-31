from django.urls import include, path

from .settings import CUSTOM_APPS

urlpatterns = [path(f'{a}/', include(f'core.apps.{a}.urls')) for a in CUSTOM_APPS]

urlpatterns.append(path('', include('core.apps.accounts.urls')),)
