from django.shortcuts import render
from .models import Product


def ProductsView(request):
    products = Product.objects.all()
    print(products)
    context = {'products': products}
    return render(request, 'store/store.html', context)