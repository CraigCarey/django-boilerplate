from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

htmx_urlpatterns = [
    path('check-username', views.check_username, name='check-username'),
    path('check-account-type', views.check_account_type, name='check-account-type'),
    path('profile/', views.profile, name='profile'),
]

urlpatterns += htmx_urlpatterns
