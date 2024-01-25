from django.contrib import admin
from .models import Category, Costumer, Product, Order

# Register your models here.

admin.site.register(Category)
admin.site.register(Costumer)
admin.site.register(Product)
admin.site.register(Order)
