from django.conf.urls import url
import mainapp.views as mainapp

urlpatterns = [
    url(r'^$', mainapp.products, name='index'),
    url(r'^product/(?P<pk>\d+)$', mainapp.product, name='product_page'),
    url(r'^category/(?P<pk>\d+)$', mainapp.products, name='category'),
    url(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)$', mainapp.products, name='category_page')



]

