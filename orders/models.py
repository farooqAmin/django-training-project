import pdb
from django.db import models

from accounts.models import UserProfile
from products.models import Product, OrderProduct

# Create your models here.


class Cart(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)


class Order(models.Model):

    IN_PROGRESS = 'In progress'
    SHIPPING = 'Shipping'
    DELIVERED = 'Delivered'

    STATUS_CHOICES = [
        (IN_PROGRESS, 'In Progress'),
        (SHIPPING, 'Shipping'),
        (DELIVERED, 'Delivered')
    ]

    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              default=IN_PROGRESS, max_length=25)
    ordered = models.BooleanField(default=False)
    customer = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(OrderProduct)
    # cart = models.OneToOneField(
    #     Cart, on_delete=models.CASCADE, related_name='order')

    def __str__(self):
        return self.customer.user.username + "order"

    def get_cart_items(self):
        if not self.ordered:
            return self.products.all().count()
        else:
            return 0

    def get_subtotal(self):
        sub_total = 0
        for order_product in self.products.all():
            sub_total += order_product.get_item_subtotal()
        return sub_total
