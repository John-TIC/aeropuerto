from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(auto_now=False, null=True)
    token = models.CharField(max_length=100, default='', null=True, blank=True)
# Para decirle al proyecto que la autenticación la va a hacer con esta clase "Usuario", nos vamos al archivo
# "settings.py" y agregamos:
# 1. AUTH_USER_MODEL = 'aeropuerto_app.Usuario' => Donde estará el modelo de autenticación de usuario, no el de Django x defecto.
# 2. 'rest_framework.authtoken', => La forma en que nos vamos a conectar a través de ese Usuario es utilizando un Token para lo
#    cual solicitamos se instale 'authtoken' para que se generen las tablas requeridas y tokens que se puedan usar.
# 3.  => En esta API vamos a tener las sgts reglas de comunicación
#        REST_FRAMEWORK = {
#            'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
#            'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
#            }
#            => La clase por defecto de permisos es 'rest_framework.permissions.IsAuthenticated'; va a preguntar si está autenticado.
#            => La clase por defecto de autenticación es 'rest_framework.authentication.TokenAuthentication'
#
class Avion(models.Model):
    codigo_avion = models.CharField(max_length=20, unique=True)
    tipo_avion = models.CharField(max_length=20)
    ciudad_base = models.CharField(max_length=20)
    marca = models.CharField(max_length=100)
    # Avion es llave foranea en otros modelos por lo que cuando se requiera en actividades de BD se debe tener claro qué información
    # deberá entregar. Esto se logra sobre-escibiendo el método __str__ para la clase (toda clase tiene un médoto __str__) cuyo
    # retorno en este caso es el campo 'codigo_avion'. ==> Defino una variable que representa el objeto completo en un select
    def __str__(self):
        return self.codigo_avion


class Piloto(models.Model):
    codigo_piloto = models.CharField(max_length=20, unique=True)
    nombre_piloto = models.CharField(max_length=50)
    horas_vuelo_piloto = models.IntegerField()
    def __str__(self):
        return self.nombre_piloto


class Tripulacion(models.Model):
    codigo_tripulante = models.CharField(max_length=20, unique=True)
    nombre_tripulante = models.CharField(max_length=50)


class Vuelo(models.Model):
    avion = models.ForeignKey(Avion, on_delete=models.PROTECT)
    piloto = models.ForeignKey(Piloto, on_delete=models.PROTECT)
    numero_vuelo = models.CharField(max_length=20, unique=True)
    origen = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)


class Itinerario(models.Model):
    vuelo = models.ForeignKey(Vuelo, on_delete=models.PROTECT)
    tripulacion = models.ForeignKey(Tripulacion, on_delete=models.PROTECT)
    cod_itinerario = models.CharField(max_length=20, unique=True)
