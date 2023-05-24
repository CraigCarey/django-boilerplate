from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('home/', views.home, name='home'),
    path('profile/', views.home, name='profile'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('register/', views.sign_up, name='register')
]
