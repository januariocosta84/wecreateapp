from django.contrib import admin
#from email_login import useradmin, adminsite
from .models import Produto, Fornesedor, Employer,Titulo,Order

# Register your models here.
#from email_login import useradmin, adminsite
#site = adminsite.EmailLoginAdminSite()
# duplicate the normal admin's registry until ticket #8500 get's fixed
#site._registry = admin.site._registry
admin.site.register(Produto)
admin.site.register(Fornesedor)
admin.site.register(Employer)
admin.site.register(Titulo)
admin.site.register(Order)