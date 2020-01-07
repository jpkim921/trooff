from django.contrib import admin

# Register your models here.
from .models import Donors, Donations

admin.site.register(Donors)
