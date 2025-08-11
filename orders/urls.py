from django.urls import path
from .views import *
from . import views 

urlpatterns = [
    path('add-to-cart/<int:product_id>/',views.add_to_cart,name="add_to_cart")
]