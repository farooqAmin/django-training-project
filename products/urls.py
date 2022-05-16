from django.urls import path
from .views import ProductView, ProductDetail, add_to_cart, productList, remove_from_cart


urlpatterns = [

    path('', productList, name='products'),
    path('add/', ProductView.as_view(), name='add-product'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
    path('<slug:slug>/update/', ProductView.as_view(), name='product-update'),
    path('<slug:slug>/delete/', ProductView.as_view(), name='product-delete'),
    path('add-to-cart/<slug:slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug:slug>/',
         remove_from_cart, name='remove-from-cart')
]
