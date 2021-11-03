from django.shortcuts import render, redirect
from .carro import Carro 
from tienda.models import Producto

# Create your views here.


def agregar(request, id):
    carro = Carro(request)
    producto = Producto.objects.get(id=id)
    carro.agregar(producto=producto)
    return redirect("tienda")

def eliminar(request, id):
    carro = Carro(request)
    producto = Producto.objects.get(id=id)
    carro.eliminar(producto=producto)
    return redirect("tienda")    

def restar(request, id):
    carro = Carro(request)
    producto = Producto.objects.get(id=id)
    carro.restar(producto=producto)
    return redirect("tienda")    

def vaciar(request, id):
    carro = Carro(request)
    carro.vaciar()
 
    return redirect("tienda")    