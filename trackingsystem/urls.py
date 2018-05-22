
from django.contrib import admin
from django.urls import path,re_path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('inventory/',include('inventory.urls'), name='inventory'),
]
