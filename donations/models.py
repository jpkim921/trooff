from django.db import models

# Create your models here.


class Donor(models.Model):
    first_name = models.CharField(max_length=50, default="Required")
    last_name = models.CharField(max_length=50, default="Required")
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(default=1234567890)
    cc_num = models.IntegerField(default=123412412341234)
    ccv_num = models.IntegerField(default=000)
    cc_expiration = models.CharField(max_length=10, default="MM/YYYY")

class Donation(models.Model):
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    