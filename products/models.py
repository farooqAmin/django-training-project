from unicodedata import category
from django.db import models

from accounts.models import UserProfile

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Sub-categories"
        unique_together = ['category', 'name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    sub_category = models.ForeignKey(
        SubCategory, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    vendor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    customer = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} * {self.product.name}"
