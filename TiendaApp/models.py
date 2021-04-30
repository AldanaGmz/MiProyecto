from django.db import models

# Create your models here.

class Categoria_Prod(models.Model):
    nombre= models.CharField(max_length=50)


    class Meta:
        verbose_name="categoria_prod"
        verbose_name_plural= "categorias_prod"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre= models.CharField(max_length=50)
    categoria= models.ForeignKey(Categoria_Prod, on_delete= models.CASCADE)
    imagen= models.ImageField(upload_to= "TiendaApp", null= True, blank= True)
    precio= models.FloatField()
    disponibilidad= models.BooleanField(default= True)

    class Meta:
        verbose_name= "producto"
        verbose_name_plural= "productos"

    
