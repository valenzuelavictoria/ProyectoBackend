"""
URL configuration for api_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
     path('admin/', admin.site.urls),
     #path('',include('Prueba.urls')),
     path('',include('Libro.urls'))
 ]

# from django.contrib import admin
# from django.urls import path, include
# from Libros import views as Libros_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', Libros.views.index, name='index_Libros'),  # Redirigir la raíz a la vista de índice
#     path('Libros/', include('Libros.urls'), name='Libros_rest'),
#     path('Escritor/', include('Escritor.urls'), name='Escritor_rest'),
#     path('AnioPublicacion/', include('AnioPublicacion.urls'), name='AnioPublicacion_rest'),
# ]


