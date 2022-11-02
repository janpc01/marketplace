from django.urls import path
from .views import item_list, products, checkout

app_name = 'core'

urlpatterns = [
    path('', item_list, name='item-list'),
    path('products', products, name='products'),
    path('checkout', checkout, name='checkout')
]
