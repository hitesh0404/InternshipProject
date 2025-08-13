from django.forms import ModelForm
from accounts.models import Address
from .models import Order
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['address']
    def __init__(self, *args, **kwargs):
        user=kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['address'].queryset = Address.objects.filter(user = user)