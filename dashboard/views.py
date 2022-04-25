from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'includes/dashboard.html')


def login(request):
    return render(request, 'includes/login.html')


def register(request):
    return render(request, 'includes/register.html')
