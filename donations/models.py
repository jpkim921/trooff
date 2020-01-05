from django.db import models

# Create your models here.


class Donation(models.Model):
    donor_name = models.CharField(max_length=50, default="anonymous")
    email = models.EmailField(unique=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    date = models.DateField(auto_now_add=True)
