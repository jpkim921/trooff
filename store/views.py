from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

from .filters import ProductFilter


def ProductsView(request):
    products = Product.objects.all()

    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs

    context = {
        'myFilter': myFilter,
        'products': products
    }
    return render(request, 'store/store.html', context)


def ProductView(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'store/product.html', context)


def CreateProduct(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('storehome')
    context = {'form': form}
    return render(request, 'store/form.html', context)


def EditProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('storehome')
    context = {'form': form}
    return render(request, 'store/form.html', context)


def DeleteProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == "POST":
        product.delete()
        return redirect('storehome')

    context = {'product': product}
    return render(request, 'store/delete.html', context)
