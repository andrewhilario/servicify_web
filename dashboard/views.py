from django.shortcuts import render
from .forms import RegistrationForm, MainUserRegistrationForm
from .tokens import account_activation_token
from .models import MainUser
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

# Create your views here.


def dashboard(request):
    return render(request, 'includes/dashboard.html')


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




def workoffer(request):
    return render(request, 'includes/workoffer.html')
    
def workoffer2(request):
    return render(request, 'includes/workoffer2.html') 

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


def service_request(request):
    return render(request, 'includes/service-request.html')

def view_service(request):
    return render(request, 'includes/view-service.html')