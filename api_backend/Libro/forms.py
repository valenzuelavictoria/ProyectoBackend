from django import forms
from Libro.models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            'nombre',
            'autor',
            'publicacion',
        ]
