from django.contrib import admin
from Libro.models import Libro, Escritor, AnioPublicacion

# Register your models here.

admin.site.register(Libro)
admin.site.register(Escritor)
admin.site.register(AnioPublicacion)