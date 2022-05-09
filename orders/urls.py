from django.urls import path, include
from .views import orderList

urlpatterns = [

    path('', orderList, name='orders'),
]
