from django.shortcuts import render, redirect
from .forms import Formulario_Contacto
from django.core.mail import EmailMessage

# Create your views here.


def contacto(request):
    formulario_contacto=Formulario_Contacto()
    if request.method=="POST":
        formulario_contacto= Formulario_Contacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            apellido=request.POST.get("apellido")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email= EmailMessage("Mensaje desde app Django", "El usuario con nombre {} apellido {} con el correo {} escribió lo sifuiente: \n\n {}".format (nombre, apellido, email, contenido), "", ["aldanaflorencia.gomez@gmail.com"], reply_to= [email])
            
            try:
                email.send()
                return redirect("/ContactoApp/?valido")

            except:
                return redirect("/ContactoApp/?novalido")
    
    return render(request, "ContactoApp/contacto.html", {'mi_formulario': formulario_contacto})
