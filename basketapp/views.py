from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from mainapp.models import Products
from basketapp.models import Basket, get_basket

@login_required
def basket(requset):
    title = 'Basket'
    basket_items = get_basket(requset.user)
    context = {
        'title': title,
        'basket_items': basket_items
    }
    return render(requset, 'basketapp/basket_page.html', context)

@login_required
def basket_add(requset, pk):
    product = get_object_or_404(Products, pk=pk)
    old_item = Basket.objects.filter(user_id=requset.user.id, product_id=product.id)

    if old_item:
        old_item[0].quantity += 1
        old_item[0].save()
    else:
        Basket.objects.create(
            user_id=requset.user.id,
            product_id=product.id,
            quantity=1
        )
    return HttpResponseRedirect(requset.META.get('HTTP_REFERER'))

@login_required
def basket_remove(requset, pk):
    items_to_delete = get_object_or_404(Basket, pk=pk)
    items_to_delete.delete()
    return HttpResponseRedirect(reverse('basket:basket_view'))
