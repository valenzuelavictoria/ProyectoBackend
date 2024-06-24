from django.urls import path
from Libro import views

urlpatterns = [
    path('index_Libro/', views.index_Libro, name='index_Libro'),
    path('Libro/', views.Libro_rest, name= 'Libro_rest'),
    path('Escritor/', views.Escritor_rest, name='Escritor_rest'),
    path('AnioPublicacion/', views.AnioPublicacion_rest, name='AnioPublicacion_rest'),
]
