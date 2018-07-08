from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum

from mainapp.models import Products

User = get_user_model()


class Basket(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    add_datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        items = Basket.objects.filter(user_id=self.user_id)
        return items.aggregate(total=Sum('quantity'))['total']

    @property
    def total_cost(self):
        items = Basket.objects.filter(user_id=self.user_id)
        return sum(list(map(lambda x: x.product_cost, items)))


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []