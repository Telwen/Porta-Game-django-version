from django.conf.urls import url
import adminapp.views as adminapp

urlpatterns = [
    url(r'users/create/$', adminapp.UserCreateView.as_view(), name='user_create'),
    url(r'users/read/$', adminapp.UserListView.as_view(), name='user'),
    url(r'users/update/(?P<pk>\d+)/$', adminapp.UserUpdateView.as_view(), name='user_update'),
    url(r'users/delete/(?P<pk>\d+)/$', adminapp.UserDeleteView.as_view(), name='user_delete'),

    url(r'categories/create/$', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
    url(r'categories/read/$', adminapp.CategoryListView.as_view(), name='categories'),
    url(r'categories/update/(?P<pk>\d+)/$', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),
    url(r'categories/delete/(?P<pk>\d+)/$', adminapp.ProductCategoryDeleteView.as_view(), name='category_delete'),

    url(r'products/create/category/(?P<category_id>\d+)/$', adminapp.ProductCreateView.as_view(), name='products_create'),
    url(r'products/read/category/(?P<category_id>\d+)/$', adminapp.products, name='products'),
    url(r'products/read/(?P<pk>\d+)/$', adminapp.ProductDetailView.as_view(), name='product_read'),
    url(r'products/update/(?P<pk>\d+)/$', adminapp.ProductUpdateView.as_view(), name='product_update'),
    url(r'products/delete/(?P<pk>\d+)/$', adminapp.ProductDeleteView.as_view(), name='product_delete'),
]

