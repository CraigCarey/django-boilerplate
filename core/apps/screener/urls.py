from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='screener-home'),
    path('table/', views.PandasHTMxTableView.as_view(), name='pandas_htmx'),
]
