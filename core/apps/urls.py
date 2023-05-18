from django.urls import include, path

urlpatterns = [
    path('accounts/', include('core.apps.accounts.urls')),
]
