from django.conf.urls import url, include
from django.contrib import admin
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', mainapp.index, name='index'),
    url(r'^contacts/', mainapp.contacts, name='contacts'),
    url(r'^products/', include('mainapp.urls', namespace='products')),
    url(r'^basket/', include('basketapp.urls', namespace='basket')),
    url(r'^store/', mainapp.store, name='store'),
    url(r'^auth/', include('authapp.urls', namespace='auth')),
    url(r'^admin/', include('adminapp.urls', namespace='admin')),
    url(r'^django_admin/', admin.site.urls, name='django_admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
