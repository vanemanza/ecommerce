from django.shortcuts import render, redirect
from .forms import FormularioContacto 
from django.core.mail import EmailMessage


# Create your views here.


def contacto(request):
    form = FormularioContacto()

    if request.method == "POST":
        form = FormularioContacto(data=request.POST)
        if form.is_valid:
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            mensaje = request.POST.get("mensaje")

            email = EmailMessage('Mensaje desde la App Ecommerce', 
                    "El Usuario {}, del mail {} escribió : {}".format(nombre, email, mensaje),
                     "",
                     ["pruebasdev15@gmail.com"], 
                     )
           
            try:
                email.send()       
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?NoValido")

    contexto = {'form': form}
    
    return render(request, 'contacto/contacto.html', contexto)

    