from django.shortcuts import render
from django.http import HttpResponse

# --- Para Generar PDF
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template

from django.contrib.auth.decorators import login_required

from ventas.models import Clientes, EstadoProducto, Categorias, Ventas

# Create your views here.

#@login_required(login_url='/account/login/')
def index(request):
    return render(request, 'home.html')

def nuevaventa(request):
    ventas = Ventas.objects.all()
    clientes = Clientes.objects.all()
    data = {'vehiculos': ventas, 'clientes': clientes}
    return render(request, "ventas/venta.html", data)


def agregarProducto(request):
    estado_producto = EstadoProducto.objects.all()
    categorias = Categorias.objects.all()
    data = {'estadoProducto': estado_producto, 'categorias': categorias}

    return render(request, 'ventas/prueba.html', data)
