from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
     contact = models.CharField(max_length=13)
     gender = models.CharField(max_length=3,choices=(
          ('M',"Male"),
          ('F',"Female"),
          ('o',"other"),
          ('N/A',"Don't Want to mention")

     ))
     user_type = models.CharField(max_length=1,choices=(
          ("S","Supplier"),
          ("C","Customer")
     ))


class Address(models.Model):
     title = models.CharField(max_length=40)
     address_line_one =models.CharField(max_length=50)
     address_line_two =models.CharField(max_length=50)
     city = models.CharField(max_length=50)
     state = models.CharField(max_length=50)
     pincode = models.IntegerField()
     user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='address')