from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .models import Product


def IndexView(request):
    products = Product.objects.all()

    return render(request, 'products/base.html', {'products': products})
