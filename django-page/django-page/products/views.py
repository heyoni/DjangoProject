from django.shortcuts import get_object_or_404, render, redirect
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
        product = Product.objects.create(title=title, price=price, description=description)
        return redirect('products:list')
    return render(request, 'products/create.html')


def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    default_view_count = product.view_counts
    product.view_counts = default_view_count + 1
    product.save()
    return render(request, 'products/detail.html', {'product':product})


def edit(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'products/edit.html', {'product':product})


def update(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=id)
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        product.title = title
        product.price = price
        product.description = description
        product.save()
        return redirect('products:detail', product.pk)

def delete(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return redirect('products:list')