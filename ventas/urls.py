from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from ventas.views import index, agregarProducto, nuevaventa

urlpatterns = [
    url(r'^$',index), #http://127.0.0.1:8000/
    path('agregar_producto/', agregarProducto),
    path('nuevaventa/', nuevaventa),
]