
from django.contrib import admin
from django.urls import path,re_path,url, include

urlpatterns = [
    url('^admin/', admin.site.urls, name='admin'),
    url('^inventory/',include('inventory.urls'), name='inventory'),
]
