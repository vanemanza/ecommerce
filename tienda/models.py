from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre =models.CharField(max_length=200, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete =models.CASCADE)
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True )
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "producto"
        verbose_name = "productos"           

    def __str__(self):
        return self.nombre    