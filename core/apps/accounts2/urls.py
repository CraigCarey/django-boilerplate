from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='root'),
    path('', include('django.contrib.auth.urls')),
    path('home', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('register', views.sign_up, name='register'),
    path('login', views.custom_login, name='login')
]
