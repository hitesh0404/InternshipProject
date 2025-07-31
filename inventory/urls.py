from django.urls import path
from .views import *
from .views import Product
from . import views 

urlpatterns = [
    path('brand/',Brand.as_view(),name="brand"),
    path('product/',Product.as_view(),name="product"),
    path('product/list',views.product_list,name="product_product_list"),
    
]