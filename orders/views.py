from django.shortcuts import render,get_object_or_404,redirect
from inventory.models import Product
from .models import Cart
from django.db.models import Q
from django.contrib import messages
# Create your views here.
def add_to_cart(request,product_id):
    product = get_object_or_404(Product,id = product_id)
    cart = Cart.objects.filter( ( Q(user = request.user) & Q( product = product)))
    if len(cart)==0:
        messages.success(request,"Item added to cart")
        Cart.objects.create(user = request.user,product = product,quantity = 1)
    else:
        cart[0].quantity +=1
        cart[0].save()
        messages.success(request,f"Cart updated with Qauntity {cart[0].quantity } ")
    return redirect('product_details',product_id)