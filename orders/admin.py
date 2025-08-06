from django.contrib import admin
from .models import Order,Orderitem,Cart,OrderStatus,Shipping,Discount,OrderRefund
admin.site.register([Order,Orderitem,Cart,OrderStatus,Shipping,Discount,OrderRefund])
# Register your models here.
