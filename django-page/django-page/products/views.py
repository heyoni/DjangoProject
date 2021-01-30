from django.shortcuts import render, redirect
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products' : products})

# Create your views here.
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        product = Product(title=title, price=price, description=description)
        product.save()

        return redirect('products:list')
    return render(request, 'products/create.html')


def product_detail(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'products/detail.html', {'product':product})


def edit(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'products/edit.html', {'product':product})


def update(request, id):
    if request.method == "POST":
        product = Product.objects.get(pk=id)
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        product.title = title
        product.price = price
        product.description = description
        product.save()
        return redirect('products:detail', product.pk)

        