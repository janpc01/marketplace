from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item


class HomeView(ListView):
    model = Item
    template_name = "home-page.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "product.html", context)


def checkout(request):
    return render(request, "checkout-page.html")
