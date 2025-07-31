from django.shortcuts import render ,redirect
from django.views import View
from .forms import Brandcrateform
from .forms import Productcrateform
from .models import Product as ProductModel
# Create your views here.
class Brand (View):
     def get(self,request):
          form = Brandcrateform()
          context={
               'form':form
          }
          return render(request,'inventory/createbrand.html',context)
     def post(self,request):
         form = Brandcrateform(request.POST)
         if form.is_valid():
              form.save()
              return redirect('home')
         else:
            context={
               'form':form
             }
            return render(request,'inventory/createbrand.html',context)  
         
class Product (View):
     def get(self,request):
          form = Productcrateform()
          context={
               'form':form
          }
          return render(request,'inventory/createproduct.html',context)
     def post(self,request):
         form = Productcrateform(request.POST)
         if form.is_valid():
              form.save()
              return redirect('home')
         else:
            context={
               'form':form
             }
            return render(request,'inventory/createproduct.html',context)  
     
def product_list(request):
     products = ProductModel.objects.all()
     context={
          'products':products
          }
     return render(request,'inventory/product_list.html',context)

     
