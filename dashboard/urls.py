from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('acquireservice/', views.acquireservice, name='acquireservice'),
    path('acquireservice2/', views.acquireservice2, name='acquireservice2'),
    path('workoffer/', views.workoffer, name='workoffer'),
    path('workoffer2/', views.workoffer2, name='workoffer2'),
]
