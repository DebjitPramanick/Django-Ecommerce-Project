from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json

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
    data = json.loads(req.body)
    productId = data['productId']
    action = data['action']

    customer = req.user.customer
    product = Product.objects.get_or_create(customer=customer, complete=False)
    order, created = Order.objects.get_or_create(order=order, product=product)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Itam was added.', safe=False)