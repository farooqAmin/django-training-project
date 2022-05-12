import pdb
from django import views
from django.utils.text import slugify
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from accounts.models import UserProfile
from .forms import ProductForm
from orders.models import Order
from .models import OrderProduct, Product

# Create your views here.


@login_required(login_url='login')
def productList(request):
    context = {}
    return render(request, 'products/products.html', context)


class ProductView(views.View):
    def get_object(self, slug):
        return Product.objects.get(slug=slug, vendor=self.request.user.userprofile)

    def get(self, request, *args, **kwargs):
        if kwargs.get('slug'):
            product = self.get_object(kwargs['slug'])
            form = ProductForm(request.POST or None, instance=product)
        else:
            form = ProductForm()
        context = {
            'form': form
        }

        return render(request, 'products/product_form.html', context)

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.userprofile
            product.slug = slugify(form.cleaned_data['name'])
            product.save()

        return redirect("home")

    def put(self, request, *args, **kwargs):

        product = self.get_object(kwargs['slug'])
        form = ProductForm(request.PUT or None, instance=product)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.userprofile
            product.slug = slugify(form.cleaned_data['name'])
            product.save()

        return redirect("home")

    def delete(self, request, *args, **kwargs):

        product = self.get_object(kwargs['slug'])
        product.delete()

        return redirect("home")


class ProductDetail(views.View):

    def get_object(self, slug):
        if self.request.user.userprofile.type == UserProfile.CUSTOMER:
            return Product.objects.get(slug=slug)
        else:
            return Product.objects.get(slug=slug, vendor=self.request.user.userprofile)

    def get(self, request, *args, **kwargs):
        product_slug = kwargs['slug']
        product = self.get_object(product_slug)

        context = {
            'product': product
        }

        return render(request, 'products/product_detail.html', context)


@login_required(login_url='login')
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)

    order_item, created = OrderProduct.objects.get_or_create(
        product=product, ordered=False, customer=request.user.userprofile)

    order_qs = Order.objects.filter(
        customer=request.user.userprofile, ordered=False)
    if order_qs.exists():
        order = order_qs.last()
        order1 = order_qs[0]

        if order.products.filter(product__slug=product.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.products.add(order_item)
    else:
        order = Order.objects.create(customer=request.user.userprofile)
        order.products.add(order_item)

    return redirect("product-detail", slug=slug)


@login_required(login_url='login')
def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        customer=request.user.userprofile, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.products.filter(product__slug=product.slug).exists():
            order_item = OrderProduct.objects.filter(
                product=product, ordered=False, customer=request.user.userprofile)[0]
            order.products.remove(order_item)
        else:
            redirect("product-detail", slug=slug)
    else:
        return redirect("product-detail", slug=slug)

    return redirect("product-detail", slug=slug)
