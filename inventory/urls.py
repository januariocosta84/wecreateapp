from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index, name='index'),
    path('produto/',views.produto, name='produto'),
    path('employer/',views.employerlist, name='employer'),
    path('staff/',views.employersearch,name='employersearch'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page': 'login'}, name='logout'),

    
]




"""
re_path('^teste/(?P<pk>\d+)/$', views.teste),
    path('registar/', views.registar, name='registar'),
    path('consultar/',views.consultar, name='consultar'),
    path('search/',views.search, name='search'),
    path('employer/',views.employerlist, name='employer'),
    path('signup/',views.signup,name='signup'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page': 'login'}, name='logout'),
    #path('login/',views.login, name='login')
   # path(r'account/', include('email_login.urls'))
"""