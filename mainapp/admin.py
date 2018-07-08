from django.contrib import admin
from mainapp.models import ProductCategory, Products

admin.site.register(Products)
admin.site.register(ProductCategory)