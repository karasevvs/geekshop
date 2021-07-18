from django.shortcuts import render
from products.models import ProductCategory, Product


# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all()
    }
    if category_id:
        context['products'] = Product.objects.filter(category_id=category_id)
    else:
        context['products'] = Product.objects.all()
    return render(request, 'products/products.html', context)
