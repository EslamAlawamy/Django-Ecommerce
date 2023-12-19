from django.shortcuts import render
from .models import Product

# Create your views here.

def products(request):
    pass

def product(request):
    return render(request, 'products/product.html')