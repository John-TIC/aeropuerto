from rest_framework import serializers
from aeropuerto_app.models import *

class Avion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Avion
        fields = '__all__'

class Piloto_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'

class Tripulacion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tripulacion
        fields = '__all__'

class Vuelo_Serializer(serializers.ModelSerializer):
    avion = Avion_Serializer(read_only=True)
    avion_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Avion.objects.all(), source='avion')
    piloto = Piloto_Serializer(read_only=True)
    piloto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Piloto.objects.all(), source='piloto')
    class Meta:
        model = Vuelo
        fields = '__all__'

class Itinerario(serializers.ModelSerializer):
    vuelo = Vuelo_Serializer(read_only=True)
    vuelo_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Vuelo.objects.all(), source='vuelo')
    tripulacion = Tripulacion_Serializer(read_only=True)
    tripulacion_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Tripulacion.objects.all(), source='tripulacion')
    class Meta:
        model = Itinerario
        fields = '__all__'

