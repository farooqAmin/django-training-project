import pdb
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

from .models import Address, UserProfile

User = get_user_model()


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateUserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['phone_number', 'type']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['mail_address', 'city', 'state', 'zip_code']
