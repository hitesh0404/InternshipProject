from django.forms import ModelForm
from .models import Brand , Product
class Brandcrateform (ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        
class Productcrateform (ModelForm):
    class Meta:
        model = Product
        fields = '__all__'