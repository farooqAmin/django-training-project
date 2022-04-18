from django.contrib import admin
from .models import Address, UserProfile

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Address)
