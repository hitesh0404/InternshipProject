from django.forms import ModelForm
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email',]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField( max_length=25,widget=forms.PasswordInput)
   
