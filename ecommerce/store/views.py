from django.shortcuts import render

# Create your views here.


# Store function for rendering store view

def store(req):
    context = {}
    return render(req, 'store/store.html', context)


# Cart function for rendering cart view

def cart(req):
    context = {}
    return render(req, 'store/cart.html', context)


# Checkout function for rendering checkout view

def checkout(req):
    context = {}
    return render(req, 'store/checkout.html', context)
