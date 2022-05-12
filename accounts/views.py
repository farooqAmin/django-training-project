import pdb
from unicodedata import combining
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import UserProfile

from .forms import AddressForm, CreateUserForm, CreateUserProfileForm
from products.models import Product

# Create your views here.


def registerPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        profile_form = CreateUserProfileForm()
        address_form = AddressForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            profile_form = CreateUserProfileForm(request.POST)
            address_form = AddressForm(request.POST)

            if form.is_valid() and profile_form.is_valid() and address_form.is_valid():
                user = form.save(commit=False)
                user.save()

                address = address_form.save(commit=False)
                address.save()

                profile = profile_form.save(commit=False)
                profile.user = user
                profile.address = address
                profile.save()

                messages.success(
                    request, 'Account created for ' + user.username)
                # messages.add_message(request, messages.INFO,
                #                      'Account created successfully')
                return redirect('login')

        context = {
            'form': form,
            'profile_form': profile_form,
            'address_form': address_form
        }
        return render(request, 'accounts/register.html', context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login as " + username)
                return redirect('home')
            else:
                messages.info(request, "Username or Password is incorrect.")

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    if request.user.userprofile.type == UserProfile.VENDOR:
        products = Product.objects.filter(vendor=request.user.userprofile)
    else:
        products = Product.objects.all()

    context = {'products': products}
    return render(request, 'accounts/home.html', context)
