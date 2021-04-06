from django.shortcuts import render, redirect
from .forms import Formulario_Contacto

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
            return redirect("/ContactoApp/?valido")
    
    return render(request, "ContactoApp/contacto.html", {'mi_formulario': formulario_contacto})
