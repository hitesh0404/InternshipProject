from django.urls import path
from .views import *
from . import views 

urlpatterns = [
    path('brand/',views.BrandCreate.as_view(),name="brand_create"),
    path('product/',views.ProductCreate.as_view(),name="product_create"),
    path('product/list/',views.product_list,name="product_list"),
    path('brand/list/',views.brand_list,name="brand_list"),
    path('search/',views.search_product,name='search_product')

    
]