from django.db import models

# Create your models here.

class Escritor(models.Model):
    nombre = models.CharField(max_length=128)
    nacionalidad = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre

class AnioPublicacion(models.Model):
    anio = models.IntegerField()

    def __str__(self):
        return self.anio

    
class Libro(models.Model):
    nombre = models.CharField(max_length=128)
    publicacion = models.ManyToManyField(AnioPublicacion, blank=True)
    autor = models.ForeignKey(Escritor, on_delete=models.CASCADE)
    #funkos = models.ManyToManyField(Funko, blank=True)

    def __str__(self):
        return self.nombre
