from django.shortcuts import render,get_object_or_404,redirect
from inventory.models import Product
from .models import Cart
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
def view_cart(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request,'orders/cart.html',{'cart':cart})

@login_required
def increment_quantity(request,product_id):
    product = get_object_or_404(Product,id = product_id)
    cart = Cart.objects.filter( ( Q(user = request.user) & Q( product = product)))
    if len(cart)>0:
        messages.success(request,f"Cart updated with Qauntity {cart[0].quantity } ")
        cart[0].quantity +=1
        cart[0].save()
    else:
        messages.error(request,"don't have that product in your cart")
    return redirect('view_cart')

@login_required
def decrement_quantity(request,product_id):
    product = get_object_or_404(Product,id = product_id)
    cart = Cart.objects.filter( ( Q(user = request.user) & Q( product = product)))
    if len(cart)>0:
        messages.success(request,f"Cart updated with Qauntity {cart[0].quantity } ")
        if cart[0].quantity == 1 :
            cart[0].delete()
        else:
            cart[0].quantity -=1
            cart[0].save()
    else:
        messages.error(request,"don't have that product in your cart")
    return redirect('view_cart')


@login_required
def remove_item(request,product_id):
    product = get_object_or_404(Product,id = product_id)
    cart = Cart.objects.filter( ( Q(user = request.user) & Q( product = product)))
    if len(cart)>0:
        messages.success(request,f"Item Removed")
        cart[0].delete()
    else:
        messages.error(request,"don't have that product in your cart")
    return redirect('view_cart')














from django.views.decorators.csrf import csrf_exempt
import uuid
import razorpay
from accounts.models import User
from .models import Orderitem
from django.conf import settings
from django.http import HttpResponseBadRequest
from payments.models import Payment
from .models import Order
from .forms import OrderForm

@login_required
def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            od_id=uuid.uuid4().hex
            order_obj = form.save(commit=False)
            order_obj.uuid = str(od_id)   
            order_obj.save()
            cust_obj = User.objects.get(username=request.user)
            # cust_obj = Customer.objects.get(user=user_obj.id)
            cart_obj = Cart.objects.filter(user = cust_obj )
            total=0
            for item in cart_obj:
                price= Product.objects.get(id = item.product.id).price
                total = total + (item.quantity * price)
                order_item_obj = Orderitem(order=order_obj,product=item.product,quantity = item.quantity,price  =price)
                order_item_obj.save()
            # cart_obj.delete()
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

            order_obj.total = int(total*100)

            data = { "amount": (int(total*100)), "currency": "INR", "receipt": order_obj.uuid }
            payment = client.order.create(data=data)
            order_obj.payment_id = payment.get('id')       
            order_obj.save()
            context = {
                'order':order_obj,
                'total':total,
                'payment':payment   
            }
            return render(request,'cart/payment.html',context)
    else:
        form = OrderForm()
        if (request.user.address.all()):
            return redirect('add_address')
        else:    
            return render(request,'cart/checkout.html',{'form':form})

@csrf_exempt
@login_required
def success(request):
    if request.method == "POST":
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        params_dict = {
            'razorpay_order_id': request.POST.get('razorpay_order_id'),
            'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
            'razorpay_signature': request.POST.get('razorpay_signature')
        }

        try:
            client.utility.verify_payment_signature(params_dict)
            cust_obj = User.objects.get(username=request.user)
            order_id = params_dict['razorpay_order_id']
            print(order_id)
            order = Order.objects.get(payment_id=order_id)
            amount = order.total
            payment_method = 'RazorPay'
            Payment.objects.create(
                user=cust_obj,
                payment_signature=params_dict['razorpay_signature'],
                amount=amount / 100,  
                status='completed',
                method=payment_method,
                order=order
            )

            # cust_obj = Customer.objects.get(user=user_obj.id)
            cart_obj = Cart.objects.filter(user=cust_obj)
            cart_obj.delete()

            
            return render(request, 'cart/success.html')
        
        except razorpay.errors.SignatureVerificationError:
            return HttpResponseBadRequest("Signature verification failed")
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    return HttpResponseBadRequest("Invalid request")
