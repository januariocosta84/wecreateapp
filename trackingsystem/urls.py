
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('^admin/', admin.site.urls, name='admin'),
    url('^inventory/',include('inventory.urls'), name='inventory'),
]
