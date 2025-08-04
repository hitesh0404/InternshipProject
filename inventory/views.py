from django.shortcuts import render ,redirect,get_object_or_404
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


def product_details(request,id):
     product = get_object_or_404(Product,id=id)
     context = {
          'product':product
     }
     return render(request,'inventory/product_details.html',context)
def product_delete(request,id):
     product = get_object_or_404(Product,id=id)
     
def product_update(request,id):
     product = get_object_or_404(Product,id=id)
     if request.method == "POST":
          form = Productcrateform(request.POST,instance=product)
          if form.is_valid():
               form.save()
               return redirect('product_details' ,id)
          else:
               context={
                    'form':form
               }
               return render(request,'inventory/product_update.html',context)
     elif request.method == "GET":
          form = Productcrateform(instance=product)
          context={
               'form':form
          }
          return render(request,'inventory/product_update.html',context)

def product_delete(request,id):
     product = get_object_or_404(Product,id=id)
     if request.method == "POST":
          product.delete()
          return redirect('product_list')
     elif request.method == "GET":
          context={
               'product':product
          }
          return render(request,'inventory/product_delete_confirmation.html',context)