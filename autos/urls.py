from django.urls import path

from . import views

urlpatterns = [
    path('clientes', views.clientes, name='clientes'),
    path('autos', views.autos, name='autos'),    
]