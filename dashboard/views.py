from multiprocessing import context
from django.shortcuts import render
from .forms import *
from .tokens import account_activation_token
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Sum
from django.http import *
import random

# for 404 page


# Create your views here.

def page_not_found(request, exception, template_name='page-not-found.html'):
    return render(request, template_name)


def dashboard(request):
    # for work offers
    work_offers = WorkOffer.objects.order_by('?')[:5]

    # for services
    service = Service.objects.order_by('?')[:5]

    context = {
        'work_offers': work_offers,
        'services': service,
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
        workOfferForm = CreateWorkOfferForm(request.POST)
        if workOfferForm.is_valid():
            work_offer = workOfferForm.save(commit=False)
            work_offer.created_by = request.user.mainuser
            work_offer.status = 'OPEN'
            work_offer.save()

            for work_offer_img in request.FILES.getlist('file'):
                pic = WorkOfferImage()
                pic.workoffer = work_offer
                pic.image = work_offer_img
                pic.save()

            context = {
                'work_offer_client': '{0} {1}'.format(request.user.first_name, request.user.last_name),
                'work_offer_name': work_offer.work_name,
                'work_offer_price': work_offer.min_pay,
                'work_offer_description': work_offer.description,
                'work_offer_imgs': WorkOfferImage.objects.filter(workoffer=work_offer)
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


def work_offer_list(request):
    work_offers = WorkOffer.objects.order_by('?')

    context = {
        'work_offers': work_offers
    }
    return render(request, 'includes/work-offer-list.html', context)

def work_offer_bidding(request, work_offer_id):
    work_offer = WorkOffer.objects.get(id=work_offer_id)
    client_work_posted = WorkOffer.objects.filter(created_by=work_offer.created_by).count()
    highest_bid = Bid.objects.filter(workoffer_id=work_offer.id).order_by('-bid_amount').first()
    total_bids = Bid.objects.filter(workoffer_id=work_offer.id).count()
    active_bids = Bid.objects.filter(workoffer_id=work_offer.id, status='PENDING').count()
    bids = Bid.objects.filter(workoffer_id=work_offer.id).order_by('-created_at').all()
    winning_bid = Bid.objects.filter(workoffer_id=work_offer.id, status='ACCEPTED').first()
    latest_bid = None
    if bids:
        latest_bid = bids[0]

    if request.user.is_authenticated:
        form = CreateWorkOfferBidForm()
    else:
        form = None

    form_errors = []
    if request.method == 'POST' and request.user.is_authenticated:
        if winning_bid:
            form_errors.append('Bidding is already closed.')

        bidForm = CreateWorkOfferBidForm(request.POST)
        if bidForm.is_valid():
            if bidForm.cleaned_data["bid_amount"] < work_offer.min_pay:
                form_errors.append('Bid amount must be greater than starting bid.')
            else:
                bid = bidForm.save(commit=False)
                bid.bidder_id = request.user.mainuser
                bid.workoffer_id = work_offer
                bid.status = 'PENDING'
                bid.save()
                return HttpResponseRedirect(work_offer_id)

    context = {
        'work_offer': work_offer,
        'client_work_posted': client_work_posted,
        'bid_form': form,
        'form_errors': form_errors if form_errors else None,
        'highest_bid': highest_bid,
        'total_bids': total_bids,
        'active_bids': active_bids,
        'latest_bid': latest_bid,
        'winning_bid': winning_bid,
        'bids': bids,
    }
    return render(request, 'includes/work-offer-bidding.html', context)

@login_required
def view_bidding_details(request, work_offer_id, bidding_id):
    bid = Bid.objects.get(id=bidding_id,workoffer_id=work_offer_id)
    is_valid_workoffer = bid.workoffer_id.status == 'OPEN'
    bidder_service = Service.objects.filter(created_by=bid.bidder_id.id).first()

    form_error = None
    if is_valid_workoffer and request.method == 'POST':
        if request.POST.get('accept-bid', False):
            bid.status = 'ACCEPTED'
            bid.workoffer_id.status = 'CLOSED'
            bid.save()
            bid.workoffer_id.save()
        elif request.POST.get('decline-bid', False):
            bid.status = 'DECLINED'
            bid.save()
        else:
            form_error = 'Unknown action'
    
    if not is_valid_workoffer:
        form_error = 'Bidding for this work offer is now closed.'


    context = {
        'bid': bid,
        'bidder_service': bidder_service if bidder_service else None,
        'form_error': form_error,
    }
    return render(request, 'includes/work-offer-bidding-details.html', context)


@login_required
def createservice(request):
    if request.method == "POST":
        serviceForm = CreateServiceForm(request.POST)
        if serviceForm.is_valid():
            service = serviceForm.save(commit=False)
            service.created_by = request.user.mainuser
            service.save()

            for service_img in request.FILES.getlist('file'):
                pic = ServiceImage()
                pic.service = service
                pic.image = service_img
                pic.save()

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


def service_details(request, service_id):
    client_acquired_service = None
    client_acquired_service_review = None
    form = None
    review_form = None
    avg_rating = None
    form_errors = []
    form_messages = []
    review_star_filter = request.GET.get('stars', None)

    service = Service.objects.get(id=service_id)
    total_clients = ServiceClients.objects.filter(service_id=service).count()
    clients_finished = ServiceClients.objects.filter(
        service_id=service, status='COMPLETED').count()
    
    if review_star_filter != 'all':
        stars = float(review_star_filter)
        reviews = ServiceReview.objects.filter(transaction_id__service_id=service, rating__range=(stars, stars+0.9)).order_by('-created_at')
    else:
        reviews = ServiceReview.objects.filter(transaction_id__service_id=service).order_by('-created_at')


    if reviews:
        rating_sum = reviews.aggregate(Sum('rating'))['rating__sum']
        avg_rating = round(rating_sum / reviews.count(), 2)
        client_acquired_service_review = reviews.filter(transaction_id__client_id=request.user.mainuser).first()
        

    if request.user.is_authenticated:
        form = AcquireServiceForm()
        client_acquired_service = ServiceClients.objects.filter(
            service_id=service, client_id=request.user.mainuser).first()

        if client_acquired_service:
            review_form = RateServiceForm()

    if request.method == 'POST' and request.user.is_authenticated and not client_acquired_service:  # acquisition
        acquired_service_form = AcquireServiceForm(request.POST)
        if acquired_service_form.is_valid():
            acquired_service = acquired_service_form.save(commit=False)
            acquired_service.client_id = request.user.mainuser
            acquired_service.service_id = service
            acquired_service.status = 'PENDING'
            acquired_service.save()
            client_acquired_service = acquired_service
            return HttpResponseRedirect(service_id)
        else:
            form_errors.append(
                'Unable to process your request. Please check your input.')

    elif request.method == 'POST' and request.user.is_authenticated and client_acquired_service:  # review
        stars = float(request.POST.get('rating2', False))
        rating_form = RateServiceForm(request.POST)
        review_imgs = request.FILES.getlist('file')

        if rating_form.is_valid() and (stars <= 5.0 and stars >= 0) and len(review_imgs) <= 5:
            review = rating_form.save(commit=False)
            review.transaction_id = client_acquired_service
            review.rating = stars
            review.save()

            for img in review_imgs:
                pic = ServiceReviewImage()
                pic.service_review = review
                pic.image = img
                pic.save()

            client_acquired_service_review = review
            return HttpResponseRedirect(service_id)
        else:
            form_errors.append(
                'Unable to process your request. Please check your input.')
    
    context = {
        'service': service,
        'total_clients': total_clients,
        'clients_finished': clients_finished,
        'client_acquired_service': client_acquired_service,
        'client_acquired_service_review': client_acquired_service_review,
        'avg_rating': avg_rating,
        'reviews': reviews,
        'form': form,
        'review_form': review_form,
        'form_messages': form_messages,
        'form_errors': form_errors,
    }
    return render(request, 'includes/service-details.html', context)


def service_requests(request, service_id):
    service = Service.objects.get(id=service_id)
    service_clients = ServiceClients.objects.filter(service_id=service)
    form_error = None

    if request.method == 'POST':
        updated_status = request.POST.get('set-client-status', False)
        service_client_id = request.POST.get('service-client-id', False)
        service_client = ServiceClients.objects.get(id=service_client_id)
        
        if service_client.status in ['COMPLETED','DECLINED','CANCELED']:
            form_error = 'Unfortunately, we cant update the status.'

        if updated_status == 'ACCEPT' and service_client.status == 'PENDING':
            service_client.status = 'ON-GOING'
            service_client.save()
        elif updated_status == 'DECLINE' and service_client.status == 'PENDING':
            service_client.status = 'DECLINED'
            service_client.save()
        elif updated_status == 'COMPLETE' and service_client.status == 'ON-GOING':
            service_client.status = 'COMPLETED'
            service_client.save()
        elif updated_status == 'CANCEL' and service_client.status == 'ON-GOING':
            service_client.status = 'CANCELED'
            service_client.save()
        else:
            form_error = 'Invalid option.'

    context = {
        'service': service,
        'service_clients': service_clients,
        'form_error': form_error,
    }
    return render(request, 'includes/service-requests.html', context)


def service_marketplace(request):
    service = Service.objects.order_by('?')
    context = {
        'services': service,
    }
    return render(request, 'includes/service-marketplace.html', context)


def acquireservice(request):
    return render(request, 'includes/acquireservice.html')


def acquireservice2(request):
    return render(request, 'includes/acquireservice2.html')


def register(request):
    registerForm = None
    mainUserForm = None

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

            mainUserForm = MainUserRegistrationForm(
                request.POST, request.FILES, instance=user.mainuser)

            if mainUserForm.is_valid():
                main_user = mainUserForm.save(commit=False)
                main_user.save()
            else:
                print('not valid')

            return render(request, 'includes/registration-success.html', {'email': user.email})
    else:
        registerForm = RegistrationForm()
        mainUserForm = MainUserRegistrationForm()
    return render(request, 'includes/register.html', {'form': registerForm, 'mainuser_form': mainUserForm})


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


def view_service(request):
    return render(request, 'includes/view-service.html')


def contact_us(request):
    return render(request, 'includes/contact-us.html')


def search_results(request):
    return render(request, 'includes/search-results-page.html')

def contactus(request):
    return render(request, 'includes/contactus.html') 

def aboutus(request):
    return render(request, 'includes/aboutus.html') 