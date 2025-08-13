from django.urls import path
from .views import *
from . import views 

urlpatterns = [
    path('add-to-cart/<int:product_id>/',views.add_to_cart,name="add_to_cart"),
    path('view-cart/',views.view_cart,name="view_cart"),
    path('increment-quantity/<int:product_id>/',views.increment_quantity,name="increment_quantity"),
    path('decrement-quantity/<int:product_id>/',views.decrement_quantity,name="decrement_quantity"),
    path('remove-item/<int:product_id>/',views.remove_item,name="remove_item"),
    path('checkout/',views.checkout,name='checkout'),
    path('payment-success/', views.success,name = 'payment_success'),
]