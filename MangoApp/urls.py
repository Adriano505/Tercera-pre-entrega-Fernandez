from django.contrib import admin
from django.urls import path
from MangoApp.views import (
    emprendedor, 
    inversor, 
    comprador, 
    inicio,
    inversor_nuevo,
    inversor_exito,
    emprendedor_nuevo,
    emprendedor_exito,
    comprador_nuevo,
    comprador_exito,
    comprador_buscar,
    emprendedor_buscar,
    inversor_buscar,
    )

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('emprendedor/', emprendedor, name='emprender'),
    path('inversor/', inversor, name='invertir'),
    path('comprador/', comprador, name='comprar'),
    path('inversor/nuevo/', inversor_nuevo, name='inversor_nuevo'),
    path('inversor/exito/', inversor_exito, name='inversor_exito'),
    path('emprendedor/nuevo/', emprendedor_nuevo, name='emprendedor_nuevo'),
    path('emprendedor/exito/', emprendedor_exito, name='emprendedor_exito'), 
    path('comprador/nuevo/', comprador_nuevo, name='comprador_nuevo'),
    path('comprador/exito/', comprador_exito, name='comprador_exito'),
    path('comprador/buscar/', comprador_buscar, name='comprador_buscar'),
    path('emprendedor/buscar/', emprendedor_buscar, name='emprendedor_buscar'), 
    path('inversor/buscar/', inversor_buscar, name='inversor_buscar'), 
]
