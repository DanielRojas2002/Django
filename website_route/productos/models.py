from django.db import models

# Create your models here.

class Producto (models.Model):
    descripcion=models.CharField(max_length=50)
    presentacion=models.CharField(max_length=50)
    precio=models.FloatField()


    def __str__(self):
        return self.descripcion

class Sucursal(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()

    def __str__(self):
        return self.nombre

        
