from django.urls import path
from .views import *
from . import views 

urlpatterns = [
    path('brand/',views.BrandCreate.as_view(),name="brand_create"),
    path('product/',views.ProductCreate.as_view(),name="product_create"),
    path('product/list/',views.product_list,name="product_list"),
    path('brand/list/',views.brand_list,name="brand_list"),
    path('search/',views.search_product,name='search_product'),
    path('product/update/<int:id>/',views.product_update,name='product_update'),
    path('product/details/<int:id>/',views.product_details,name='product_details'),
    path('product/delete/<int:id>/',views.product_delete,name='product_delete'),

    
]