from django.db import models

# Create your models here.
class Brand(models.Model):
    name= models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name}"
    

class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,
        related_name='subcategories'
    )
    def __str__(self):
        return self.name

class Product(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10,decimal_places=2)

class ProductImages(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product")
    image = models.ImageField(upload_to='product/')
    alt_text = models.CharField(max_length=100)

