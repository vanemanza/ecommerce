from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="nombre", blank=True, null=True)
    email = models.EmailField(max_length=200, verbose_name="email", blank=True, null=True )
    telefono = models.CharField(max_length=15)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre