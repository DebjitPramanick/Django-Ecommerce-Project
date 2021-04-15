from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.


# Store function for rendering store view

def store(req):
    products = Product.objects.all()
    context = {'products': products}
    return render(req, 'store/store.html', context)


# Cart function for rendering cart view

def cart(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print(order)
        items = order.orderitem_set.all()
    else:
        ityem = [] # For non-authenticated users
        order={'get_cart_total': 0, 'get_cart_items': 0} # For non-authenticated users

    context = {'items': items, 'order': order}
    return render(req, 'store/cart.html', context)


# Checkout function for rendering checkout view

def checkout(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print(order)
        items = order.orderitem_set.all()
    else:
        ityem = [] # For non-authenticated users
        order={'get_cart_total': 0, 'get_cart_items': 0} # For non-authenticated users

    context = {'items': items, 'order': order}
    return render(req, 'store/checkout.html', context)


# Update cart items

def updateItem(req):
    return JsonResponse('Itam was added.', safe=False)