from django.urls import path
from .views import *
from .views import Product

urlpatterns = [
    path('brand/',Brand.as_view(),name="brand"),
    path('product/',Product.as_view(),name="product"),
    
    
]