from django.urls import path, include
from .views import ProductDetail, add_to_cart, productList, remove_from_cart
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path('', productList, name='products'),
    path('<slug:slug>/', login_required(ProductDetail.as_view()),
         name='product-detail'),
    path('add-to-cart/<slug:slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug:slug>/',
         remove_from_cart, name='remove-from-cart')
]
