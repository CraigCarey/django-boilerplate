from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('register_user', views.register_user, name='register_user'),
    path('logout', LogoutView.as_view(), name='logout'),
]

htmx_urlpatterns = [
    path('check-username', views.check_username, name='check-username'),
    path('check-subject', views.check_subject, name='check-subject'),
]

urlpatterns += htmx_urlpatterns
