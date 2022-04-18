from django.db import models

from accounts.models import UserProfile
from products.models import Product

# Create your models here.


class Cart(models.Model):
    customer = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)


class Order(models.Model):

    IN_PROGRESS = 'in_progress'
    SHIPPING = 'shipping'
    DELIVERED = 'delivered'

    STATUS_CHOICES = [
        (IN_PROGRESS, 'In Progress'),
        (SHIPPING, 'Shipping'),
        (DELIVERED, 'Delivered')
    ]

    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              default=IN_PROGRESS, max_length=25)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.username + "order"
