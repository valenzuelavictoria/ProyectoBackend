from rest_framework import serializers
from Libro.models import Libro, AnioPublicacion, Escritor


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('nombre',)

class AnioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnioPublicacion
        fields = ('nombre', 'artista')

class EscritorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escritor
        fields = ('nombre',)