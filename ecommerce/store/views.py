from django.shortcuts import render
from .models import *

# Create your views here.


# Store function for rendering store view

def store(req):
    products = Product.objects.all()
    context = {'products': products}
    return render(req, 'store/store.html', context)


# Cart function for rendering cart view

def cart(req):
    context = {}
    return render(req, 'store/cart.html', context)


# Checkout function for rendering checkout view

def checkout(req):
    context = {}
    return render(req, 'store/checkout.html', context)
