
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static



urlpatterns = [
    url('^admin/', admin.site.urls, name='admin'),
    url('',include('inventory.urls'), name='inventory'),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)