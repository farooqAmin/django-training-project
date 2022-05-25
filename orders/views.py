import pdb
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django import views

from products.models import Product
from .models import Order

from products.models import OrderProduct

# Create your views here.


@login_required(login_url='login')
def orderList(request):
    order_qs = Order.objects.filter(customer=request.user.userprofile)
    context = {
        'orders': order_qs
    }
    return render(request, 'orders/orders.html', context)


class Cart(views.View):

    @method_decorator(login_required(login_url='login'))
    def get(self, request, *args, **kwargs):
        context = {
            'cart_items_count': 0,
            'cart_items': {},
            'sub_total': 0
        }
        if request.user.userprofile.order_set.exists():
            context = {
                'cart_items_count': request.user.userprofile.order_set.last().get_cart_items(),
                'cart_items': request.user.userprofile.order_set.last().products.all(),
                'sub_total': request.user.userprofile.order_set.last().get_subtotal()
            }
        return render(request, 'orders/cart.html', context)


class CartProduct(views.View):

    def get_object(self, slug):
        return OrderProduct.objects.get(product__slug=slug, customer=self.request.user.userprofile, ordered=False)

    @method_decorator(login_required(login_url='login'))
    def put(self, request, *args, **kwargs):

        order_product = self.get_object(kwargs['slug'])
        product = Product.objects.get(slug=kwargs['slug'])
        action = request.PUT.get('action')

        if action == 'increment':
            order_product.quantity += 1
            order_product.save()
            product.quantity -= 1
            product.save()
        else:
            if order_product.quantity == 1:
                order = Order.objects.filter(
                    customer=request.user.userprofile, ordered=False).last()

                order.products.remove(order_product)
                order_product.delete()
                product.quantity += 1
                product.save()

            else:
                order_product.quantity -= 1
                order_product.save()
                product.quantity += 1
                product.save()

        return redirect("cart")
