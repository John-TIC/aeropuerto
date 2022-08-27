from django.shortcuts import render
from aeropuerto_app.models import *
from aeropuerto_app.serializers import *
from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.
class Usuario_view(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = Usuario_Serializer

class Avion_view(viewsets.ModelViewSet):
    #* Mixin-combinación de varios atributos que podemos usar (una clase maneja todas las peticiones POST, GET, PUT, DELETE, RETRIEVE)
    queryset = Avion.objects.all()  # De donde quiero sacar los resultados y a quienes quiero impactar.
                                    # queryset = Avion.objects.all().order_by('-codigo_avion')
    serializer_class = Avion_Serializer  # Qué serializador nos dá las reglas para poder cumplir el objetivo.

class Piloto_view(viewsets.ModelViewSet):
    queryset = Piloto.objects.all()
    serializer_class = Piloto_Serializer

class Tripulacion_view(viewsets.ModelViewSet):
    queryset = Tripulacion.objects.all()
    serializer_class = Tripulacion_Serializer

class Vuelo_view(viewsets.ModelViewSet):
    queryset = Vuelo.objects.all()
    serializer_class = Vuelo_Serializer

class Itinerario_view(viewsets.ModelViewSet):
    queryset = Itinerario.objects.all()
    serializer_class = Itinerario_Serializer

# Se está customizando la autenticación x Token que hereda de 'ObtainAuthToken'; es como decir 'Yo soy usuario reconozcame!', entonces
# deme el usuario y el password para autenticarlo.
# Se sobreescribe el método POST diciendo que cuando llegue una petición por POST a esta vista
class CustomAuthToken_view(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user.token = token.key
        user.save()
        usuario = Usuario_Serializer(user)
        return Response(usuario.data)