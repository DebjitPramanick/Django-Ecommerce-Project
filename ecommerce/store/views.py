from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
import datetime
from django.contrib.auth.models import User

# Create your views here.


# Store function for rendering store view

def store(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = [] # For non-authenticated users
        order={'get_cart_total': 0, 'get_cart_items': 0} # For non-authenticated users
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(req, 'store/store.html', context)


# Cart function for rendering cart view

def cart(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print(order)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = [] # For non-authenticated users
        order={'get_cart_total': 0, 'get_cart_items': 0} # For non-authenticated users
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(req, 'store/cart.html', context)


# Checkout function for rendering checkout view

def checkout(req):
    if req.user.is_authenticated:
        email = req.user.email
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        print(order)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = [] # For non-authenticated users
        order={'get_cart_total': 0, 'get_cart_items': 0} # For non-authenticated users
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems, 'email': email}
    return render(req, 'store/checkout.html', context)


# Update cart items

def updateItem(req):
    data = json.loads(req.body)
    productId = data['productId']
    action = data['action']

    customer = req.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)


    if action == 'add':
        print("Added")
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        print("Removed")
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added.', safe=False)

def processOrder(req):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(req.body)
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        print(data)

        ShippingModel.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
        )

        print(ShippingModel)

    else:
        print('User is not logged in.')

    return JsonResponse('Payment complete.', safe=False)