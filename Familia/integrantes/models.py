from django.db import models

# Create your models here.
class Integrante(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre, self.edad

class Auto(models.Model):
    patente = models.CharField(max_length=7)
    modelo = models.CharField(max_length=15)
    anio = models.IntegerField()
    color = models.CharField(max_length=15)

    def __str__(self):
        return self.modelo, self.patente

class Casa(models.Model):
    direccion = models.CharField(max_length=30)
    altura = models.IntegerField()

    def __str__(self):
        return self.direccion, self.altura