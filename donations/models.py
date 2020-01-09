from django.db import models

# Create your models here.


class Donor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(unique=True)
    cc_num = models.IntegerField()
    ccv_num = models.IntegerField()
    cc_expiration = models.CharField(max_length=10)

class Donation(models.Model):
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    