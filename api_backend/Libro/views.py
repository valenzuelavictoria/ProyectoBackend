from django.shortcuts import render
from django.http import JsonResponse
from Libro.models import Escritor, Libro, AnioPublicacion
from Libro.serializer import LibroSerializer, AnioSerializer, EscritorSerializer
from Libro.forms import LibroForm

#from django.views.generic import CreateView

# Create your views here.

def index_Libro(request):
     Libro = Libro.objects.all()
     Escritor = Escritor.objects.all()
     AnioPublicacion = AnioPublicacion.objects.all()

     return render(request, 'index_Libro.html', {
         'Libro': Libro,
         'Escritores': Escritor,
         'aniopublicacion': AnioPublicacion,
     })


def Libro_rest(request):
    Libro = Libro.objects.all()
    serializer = LibroSerializer(Libro, many=True)
    
    return JsonResponse(serializer.data, safe=False)

def Escritor_rest(request):
    Escritor = Escritor.objects.all()
    serializer = EscritorSerializer(Escritor, many=True)

    return JsonResponse(serializer.data, safe=False)

def AnioPublicacion_rest(request):
    Anio = Anio.objects.all()
    serializer = AnioPublicacion_rest(Anio, many=True)
    
    return JsonResponse(serializer.data, safe=False)
