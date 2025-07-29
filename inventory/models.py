from django.db import models

# Create your models here.
class Brand(models.Model):
    name= models.CharField(max_length=30)
class Product(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10,decimal_places=2)