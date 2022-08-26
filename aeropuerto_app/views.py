from django.shortcuts import render
from aeropuerto_app.models import *
from aeropuerto_app.serializers import *
from rest_framework import viewsets, status


# Create your views here.

class Avion_view(viewsets.ModelViewSet):
    #* Mixin-combinación de varios atributos que podemos usar (una clase maneja todas las peticiones POST, GET, PUT, DELETE, RETRIEVE)
    queryset = Avion.objects.all()  # De donde quiero sacar los resultados y a quienes quiero impactar.
                                    # queryset = Avion.objects.all().order_by('-codigo_avion')
    serializer_class = Avion_Serializer  # Qué serializador nos dá las reglas para poder cumplir el objetivo.
