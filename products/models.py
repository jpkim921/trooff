from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=100)
