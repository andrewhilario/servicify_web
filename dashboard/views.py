from django.shortcuts import render
from .forms import RegistrationForm, MainUserRegistrationForm, CreateWorkOfferForm, CreateServiceForm
from .tokens import account_activation_token
from .models import MainUser, WorkOffer, ServiceImage
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import *
import random

# for 404 page


# Create your views here.

def page_not_found(request, exception, template_name='page-not-found.html'):
    return render(request, template_name)




def dashboard(request):
    # for work offers
    valid_work_offers = WorkOffer.objects.filter(status='OPEN').values_list('id', flat=True)
    random_profiles_id_list = random.sample(list(valid_work_offers), min(len(valid_work_offers), 10))
    query_set = WorkOffer.objects.filter(id__in=random_profiles_id_list)
    
    context = { 
        'work_offers': query_set.all()
    }

    return render(request, 'includes/dashboard.html', context)


def avatar(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        avatar = MainUser.objects.filter(user=user)
        context = {
            "avatar": avatar,
        }
        return context
    else:
        return {
            'NotLoggedIn': User.objects.none()
        }

def logout_user(request):
    logout(request)
    return render(request, 'includes/logout.html')


def custom_logout(request, next_page="/register"):
    logout(request)
    if next_page is None:
        return render(request, 'includes/logout.html')
    else:
        return HttpResponseRedirect(next_page)



@login_required
def createworkoffer(request):
    # check_work_offer = WorkOffer.objects.filter(created_by=request.user.mainuser)
    # if check_work_offer:
    #     return render(request, 'includes/workoffer-create.html', { 'errors': 'You can only create one Work Offer each account.'})

    if request.method == "POST": 
        workOfferForm = CreateWorkOfferForm(request.POST, request.FILES)
        if workOfferForm.is_valid():
            work_offer = workOfferForm.save(commit=False)
            work_offer.created_by = request.user.mainuser
            work_offer.status = 'OPEN'
            work_offer.save()

            context = {
                'work_offer_client': '{0} {1}'.format(request.user.first_name, request.user.last_name),
                'work_offer_name': work_offer.work_name,
                'work_offer_price': work_offer.min_pay,
                'work_offer_description': work_offer.description,
                'work_offer_thumbnail_url': work_offer.thumbnail.url,
            }
            return render(request, 'includes/workoffer-success.html', context)

    form = CreateWorkOfferForm()
    context = { 
        'client_name': '{0} {1}'.format(request.user.first_name, request.user.last_name),
        'form': form
    }

    return render(request, 'includes/workoffer-create.html', context)

def workoffer(request):
    return render(request, 'includes/workoffer.html')
    
def workoffer2(request):
    return render(request, 'includes/workoffer2.html') 

@login_required
def createservice(request):
    if request.method == "POST":
        serviceForm = CreateServiceForm(request.POST)
        if serviceForm.is_valid():
            service = serviceForm.save(commit=False)
            service.created_by = request.user.mainuser
            service.save()

            print(request.FILES)
            for service_img in request.FILES.getlist('file'):
                pic = ServiceImage()
                pic.service = service 
                pic.image = service_img
                pic.save()
                print(service_img)
            
            context = {
                'service_owner': '{0} {1}'.format(request.user.first_name, request.user.last_name),
                'service': service,
                'service_imgs': ServiceImage.objects.filter(service=service)
            }
            return render(request, 'includes/service-success.html', context)

    form = CreateServiceForm()
    context = { 
        'service_owner': '{0} {1}'.format(request.user.first_name, request.user.last_name),
        'form': form
    }
    return render(request, 'includes/service-create.html', context) 

def createservice_success(request):
    return render(request, 'includes/service-success.html')

def acquireservice(request):
    return render(request, 'includes/acquireservice.html') 

def acquireservice2(request):
    return render(request, 'includes/acquireservice2.html') 

def register(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Servicify: Activate your account'
            message = render_to_string('email-activation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)

            mainUserForm = MainUserRegistrationForm(request.POST, request.FILES, instance=user.mainuser)

            if mainUserForm.is_valid():
                main_user = mainUserForm.save(commit=False)
                main_user.save()
            else:
                print('not valid')

            return render(request, 'includes/registration-success.html', {'email': user.email})
    else:
        registerForm = RegistrationForm()
        mainUserForm = MainUserRegistrationForm()
    return render(request, 'includes/register.html', {'form': registerForm,'mainuser_form':mainUserForm})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'includes/registration-complete.html', {'fullname': user.first_name + " " + user.first_name})
    else:
        return render(request, 'includes/registration-invalid.html')



def register_success(request):
    return render(request, 'includes/registration-success.html')


def profile_page(request):
    return render(request, 'includes/profile-page.html')


def profile_client(request):
    return render(request, 'includes/profile-page-client.html')


def service_request(request):
    return render(request, 'includes/service-request.html')

def view_service(request):
    return render(request, 'includes/view-service.html')


def work_offer_list(request):
    valid_work_offers = WorkOffer.objects.filter(status='OPEN').values_list('id', flat=True)
    random_profiles_id_list = random.sample(list(valid_work_offers), min(len(valid_work_offers), 10))
    query_set = WorkOffer.objects.filter(id__in=random_profiles_id_list)
    context = { 
        'work_offers': query_set.all()
    }
    return render(request, 'includes/work-offer-list.html', context)

# @login_required
def work_offer_bidding(request):
    return render(request, 'includes/work-offer-bidding.html')


def view_work_offer_bidding(request):
    return render(request, 'includes/view-work-offer-bid.html')

def contact_us(request):
    return render(request, 'includes/contact-us.html')

def search_results(request):
    return render(request, 'includes/search-results-page.html')