from django.shortcuts import render
from .carrito import Carro
from TiendaApp.models import Producto
from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, porducto_id):
    carro= Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("TiendaApp")

def eliminar_producto(request, porducto_id):
    carro= Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("TiendaApp")


def restar_producto(request, porducto_id):
    carro= Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("TiendaApp")


def limpiar_carro(request, porducto_id):
    carro= Carro(request)
    carro.limpiar_carro()
    return redirect("TiendaApp")

