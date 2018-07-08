from django.core.management.base import BaseCommand
from django.conf import settings
from mainapp.models import ProductCategory, Products
from authapp.models import ShopUser
import os
import json

BASE_JSON_PATH = os.path.join(settings.BASE_DIR, 'mainapp', 'json')


def json_loader(file_name):
    with open(os.path.join(BASE_JSON_PATH, '{}.json'.format(file_name))) as f:
        return json.load(f)


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = json_loader('categories')
        products = json_loader('products')

        ProductCategory.objects.all().delete()
        Products.objects.all().delete()

        for category in categories:
            ProductCategory.objects.create(**category)

        for product in products:
            category_name = product.pop('category')
            product_categoty = ProductCategory.objects.get(name=category_name)
            product['category_id'] = product_categoty.id
            Products.objects.create(**product)

        ShopUser.objects.all().delete()
        ShopUser.objects.create_superuser(
            username='telwen', email='kartman40@mail.ru', password='11999966', age='22'
        )
