from django.urls import path
from .views import (
    HomeView,
    ItemDetailView,
    products,
    checkout
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='item-list'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('checkout', checkout, name='checkout')
]
