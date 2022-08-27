from rest_framework import serializers
from aeropuerto_app.models import *

class Usuario_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    # Ahora cuando se cree un Usuario la información de entrada deberá validarse y si todo funciona bien, salvar el registro
    # en BD
    def create(self, validated_data):
        user = Usuario(
            username=validated_data['username'],
            email=validated_data['email'],
            telefono=validated_data['telefono'],
            direccion=validated_data['direccion'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            fecha_nacimiento=validated_data['fecha_nacimiento'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

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

class Itinerario_Serializer(serializers.ModelSerializer):
    vuelo = Vuelo_Serializer(read_only=True)
    vuelo_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Vuelo.objects.all(), source='vuelo')
    tripulacion = Tripulacion_Serializer(read_only=True)
    tripulacion_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Tripulacion.objects.all(), source='tripulacion')
    class Meta:
        model = Itinerario
        fields = '__all__'

