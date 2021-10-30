from django.shortcuts import render

# Create your views here.
def inicio(request):
    
    return render(request, 'webapp/inicio.html', {})

def blog(request):
    
    return render(request, 'webapp/blog.html', {})

def contacto(request):
    
    return render(request, 'webapp/contacto.html', {})

def servicios(request):
    
    return render(request, 'webapp/servicios.html', {})

def tienda(request):
    
    return render(request, 'webapp/tienda.html', {})