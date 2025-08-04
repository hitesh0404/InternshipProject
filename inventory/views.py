from django.shortcuts import render ,redirect
from django.views import View
from .forms import Brandcrateform
from .forms import Productcrateform
from .models import Product as Product
from .models import Brand as Brand
# Create your views here.
class BrandCreate (View):
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
         
class ProductCreate (View):
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
     products = Product.objects.all()
     context={
          'products':products
          }
     return render(request,'inventory/product_list.html',context)

def brand_list(request):
     brands = Brand.objects.all()
     context={
          'brands':brands
          }
     return render(request,'inventory/brand_list.html',context)
     
def search_product(request):
     q = request.GET.get('q')
     products = Product.objects.filter(name__icontains = q)
     context={
          'products':products
          }
     return render(request,'inventory/product_list.html',context)