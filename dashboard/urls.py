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
    path('custom_logout', views.custom_logout, name='custom_logout'),
    path('register/', views.register, name='register'),

    #services
    path('service-request/', views.service_request, name='service_request'),
    path('service-request/view/', views.view_service, name='view_service'),
    path('createservice/', views.createservice, name='createservice'),
    path('createservice/success/', views.createservice_success, name='createservice_success'),
    path('service-marketplace/', views.service_marketplace, name='service_marketplace'),
    path('acquireservice/', views.acquireservice, name='acquireservice'),
    path('acquireservice2/', views.acquireservice2, name='acquireservice2'),

    # work offers
    path('createworkoffer/', views.createworkoffer, name='createworkoffer'),
    path('workoffer/', views.work_offer_list, name='work_offer_list'),
    path('workoffer/view', views.workoffer, name='workoffer_view'),
    path('workoffer2/', views.workoffer2, name='workoffer2'),
    path('biddings/<slug:work_offer_id>', views.work_offer_bidding, name='work_offer_bidding'),
    path('biddings/view/', views.view_work_offer_bidding, name='view_work_offer_bidding'),
    
    path('register/success', views.register_success, name='register_success'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.activate, name='activate'),
    path('profile/service-person', views.profile_page, name='profile'),
    path('profile/client', views.profile_client, name='profile_client'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('search/', views.search_results, name='search_results'),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


