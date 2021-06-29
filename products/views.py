from django.shortcuts import render
import json


# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    with open('products/fixtures/products.json', 'r', encoding='utf-8') as json_file:
        json_products = json.load(json_file)
    context = {
        'title': 'GeekShop - Каталог',
        'products': json_products
    }
    return render(request, 'products/products.html', context)
