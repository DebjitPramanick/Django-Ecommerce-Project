from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('updateitem/', views.updateItem, name="updateitem"),
    path('process_order/', views.processOrder, name="processOrder"),
]