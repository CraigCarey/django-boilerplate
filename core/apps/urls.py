from django.urls import include, path

urlpatterns = [
    path('', include('core.apps.accounts.urls')),
    path('accounts/', include('core.apps.accounts.urls')),
]
