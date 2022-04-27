from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'includes/dashboard.html')


def login(request):
    return render(request, 'includes/login.html')


def register(request):
    return render(request, 'includes/register.html')


def register_details(request):
    return render(request, 'includes/register-detail.html')


def account_type(request):
    return render(request, 'includes/register-account-type.html')


def register_success(request):
    return render(request, 'includes/registration-success.html')
