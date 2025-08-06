from django.contrib import admin

# Register your models here.
from .models import Product,Brand

admin.site.register([Product,Brand])