from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


# Create your views here.

def products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 9)  # Show 2 products per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj
    }
    return render(request, 'products/products.html', context)

def product(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'products/product.html', context)