from django.shortcuts import render
from .models import *


def store(request):
    products = Product.objects.all()                #querying all the products here
    context = {'products': products}                #variable and its value are the same just for the sake of simplicity
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

