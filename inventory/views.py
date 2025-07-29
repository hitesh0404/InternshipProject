from django.shortcuts import render ,redirect
from django.views import View
from .forms import Brandcrateform
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
         
