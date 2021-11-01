from django.shortcuts import render
from .models import Producto, Categoria

# Create your views here.

def tienda(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}

    return render(request, 'tienda/tienda.html', contexto)