from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register/details', views.register_details, name='details',),
    path('register/account-type', views.account_type, name='account_type'),
    path('register/success', views.register_success, name='register_success'),
]
