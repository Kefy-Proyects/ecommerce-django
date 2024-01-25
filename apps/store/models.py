from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    parent=models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    
    class Meta:
        verbose_name_plural='categories'
        
    def __str__(self):
        return self.name

class Costumer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=150)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    description=models.CharField(max_length=200, default='', null=True, blank=True)
    image=models.ImageField(upload_to='uploads/product/')
    date_creation=models.DateField(auto_now_add=True)
    last_change=models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    costumer=models.ForeignKey(Costumer, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    address=models.CharField(max_length=250, default='', blank=True, null=True)
    status=models.BooleanField(default=False)
    phone=models.CharField(max_length=20, default='', null=True, blank=True)
    date_creation=models.DateField(auto_now_add=True)
    date=models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return str(self.product)