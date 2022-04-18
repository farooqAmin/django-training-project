from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mail_address = models.CharField("address", max_length=128)

    city = models.CharField(max_length=64, default="Lahore")
    state = models.CharField(max_length=64, default="Punjab")
    zip_code = models.CharField(max_length=5, default="54000")

    def __str__(self):
        return self.mail_address + " " + self.zip_code


class UserProfile(models.Model):

    CUSTOMER = 'customer'
    VENDOR = 'vendor'

    USER_TYPES = [
        (CUSTOMER, 'Customer'),
        (VENDOR, 'Vendor')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=20, choices=USER_TYPES, default=CUSTOMER)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(
        validators=[phoneNumberRegex], max_length=16, unique=True)

    def __str__(self):
        return self.user.username + " " + self.type
