from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import Product



def ProductsApi(request):
    products = Product.objects.all().values()
    products_list = list(products)
    return JsonResponse(products_list, safe=False)


    