from django.conf.urls import url
import basketapp.views as basketapp

urlpatterns = [
    url(r'^$', basketapp.basket, name='basket_view'),
    url(r'^add/(?P<pk>\d+)$', basketapp.basket_add, name='add'),
    url(r'^remove/(?P<pk>\d+)$', basketapp.basket_remove, name='remove')
]
