from dataclasses import fields
import pdb
from django import forms
from django.contrib.auth import get_user_model

from .models import Product

User = get_user_model()


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'sub_category', 'price', 'quantity']
