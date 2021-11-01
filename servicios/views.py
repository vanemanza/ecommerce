from django.shortcuts import render
from .models import Servicio

def servicios(request):
    
    servicios = Servicio.objects.all()
    contexto = {'servicios': servicios}

    return render(request, 'servicios/servicios.html', contexto)