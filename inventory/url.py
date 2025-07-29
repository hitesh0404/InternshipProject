from django.urls import path
from .views import *

urlpatterns = [
    path('brand/',Brand.as_view(),name="brand"),
    
    
]