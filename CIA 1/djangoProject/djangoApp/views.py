from django.shortcuts import render
from .models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()[:3]  # Fetch first 3 products
    return render(request, 'djangoApp/product_list.html', {'products': products})
