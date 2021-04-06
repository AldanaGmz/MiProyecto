from django import forms

class Formulario_Contacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True)
    apellido=forms.CharField(label="Apellido", required=True)
    email=forms.CharField(label="Email", required=True)
    contenido=forms.CharField(label="Contenido", widget= forms.Textarea)

