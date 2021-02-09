from django.shortcuts import render
from .models import *
from django.http import JsonResponse


def store(request):
    products = Product.objects.all()                #querying all the products here
    context = {'products': products}                #variable and its value are the same just for the sake of simplicity
    return render(request, 'store/store.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def UpdateItem(request):
    return JsonResponse("Item was added", safe=False)