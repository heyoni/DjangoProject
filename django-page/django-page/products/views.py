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