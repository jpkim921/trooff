from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import Product


def ProductsView(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


# def ProductPage(request, pk):
#     product = Product.objects.filter(id=pk).values()
#     data = list(product)
#     return JsonResponse(data, safe=False)
