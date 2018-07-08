from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='media_folder_products')
def media_folder_products(product_img_path):
    if not product_img_path:
        product_img_path = 'products_images/default.jpg'

    return f"{settings.MEDIA_URL}{product_img_path}"


@register.filter(name='media_folder_users')
def media_folder_users(avatar_path):
    if not avatar_path:
        avatar_path = 'avatars/default.jpg'

    return f"{settings.MEDIA_URL}{avatar_path}"
