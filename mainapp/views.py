from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from basketapp.models import Basket
from .dict.menu_links import ml
from basketapp.models import get_basket
from .models import Products, ProductCategory, last_purchase


def index(request):
    basket = get_basket(request.user)
    context = {
        'title': 'Porta-Games',
        'menu_links': ml,
        'slidebar_img': [
            'IMG/tw3sb.jpg',
            'IMG/m2033sb.jpg',
            'IMG/smsb.jpg',
            'IMG/kksb.jpg',
            'IMG/ds3sb.jpg',
        ],
        'basket': basket,
        'leaders_of_sells': last_purchase(),

    }

    return render(request, 'mainapp/index.html', context)


def contacts(request):
    basket = get_basket(request.user)
    context = {
        'title': 'Contacts',
        'menu_links': ml,
        'basket': basket
    }
    return render(request, 'mainapp/contacts.html', context)


def products(request, pk=None, page=1):
    title = 'Products'
    all_categories = ProductCategory.objects.all()
    basket = get_basket(request.user)
    all_products = Products.objects.all()
    if pk:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Products.objects.filter(category_id=pk, is_active=True, category__is_active=True).order_by('price')
        paginator = Paginator(products, per_page=2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)
        context = {
                'title': title,
                'menu_links': ml,
                'products': products_paginator,
                'menu_category': all_categories,
                'category': category,
                'basket': basket
            }
        return render(request, 'mainapp/products.html', context)
    context = {
        'basket': basket,
        'title': title,
        'menu_category': all_categories,
        'products': all_products,
        'menu_links': ml
        }
    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    item = get_object_or_404(Products, pk=pk)
    basket = get_basket(request.user)
    same_products = Products.objects.filter(category_id=item.category.id).exclude(id=item.id)

    context = {
        'item': item,
        'basket': basket,
        'menu_links': ml,
        'same_products': same_products[:4]
    }

    return render(request, 'mainapp/product.html', context)


def store(request):
    basket = get_basket(request.user)
    context = {
        'title': 'Store',
        'menu_links': ml,
        'basket': basket
    }
    return render(request, 'mainapp/store.html', context)
