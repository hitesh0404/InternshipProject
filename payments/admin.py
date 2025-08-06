from django.contrib import admin
from .models import Payment,Coupon,CouponUsage

admin.site.register([Payment,Coupon,CouponUsage])