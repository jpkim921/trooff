from django.shortcuts import render
from .models import Product


def ProductsView(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

def ProductView(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'store/product.html', context)