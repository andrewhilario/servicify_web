from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .forms import UserLoginForm


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('home/', views.dashboard, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='includes/login.html',
                                                authentication_form=UserLoginForm), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('acquireservice/', views.acquireservice, name='acquireservice'),
    path('acquireservice2/', views.acquireservice2, name='acquireservice2'),
    path('workoffer/', views.workoffer, name='workoffer'),
    path('workoffer2/', views.workoffer2, name='workoffer2'),
    path('register/details', views.register_details, name='details',),
    path('register/account-type', views.account_type, name='account_type'),
    path('register/success', views.register_success, name='register_success'),
    path('activate/<slug:uidb64>/<slug:token>)/',
         views.activate, name='activate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
