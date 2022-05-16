from django.urls import path
from .views import Cart, CartProduct, orderList

urlpatterns = [

    path('', orderList, name='orders'),
    path('cart', Cart.as_view(), name="cart"),
    path('cart-product/<slug:slug>/update/',
         CartProduct.as_view(), name="cart-product"),
]
