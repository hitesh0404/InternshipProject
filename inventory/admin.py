from django.contrib import admin

# Register your models here.
from .models import Product,Brand,Category,ProductImages

admin.site.register([Product,Brand,Category,ProductImages])