from django.forms import ModelForm
from .models import Brand
class Brandcrateform (ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'