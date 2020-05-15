from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def ProductsView(request):
    products = Product.objects.all()
    context = {'products': products}
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
