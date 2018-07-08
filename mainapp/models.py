import random

from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Name', max_length=64, unique=True)
    desc = models.TextField(verbose_name='Description', blank=True)
    is_active = models.BooleanField(verbose_name='Category condition', default=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(verbose_name='Item Name', max_length=64, unique=True)
    price = models.DecimalField(verbose_name='Item Price', decimal_places=2, max_digits=10)
    tiny_desc = models.TextField(verbose_name='Short Description')
    desc = models.TextField(verbose_name='Item Description', )
    img = models.ImageField(upload_to='products_images', blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    href = models.CharField(verbose_name='Item link', max_length=64)
    is_active = models.BooleanField(verbose_name='Productcondition', default=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)


def last_purchase():
    all_products = Products.objects.all()
    all_products = list(all_products)
    return random.choices(all_products, k=4)


def same_product():
    pass
