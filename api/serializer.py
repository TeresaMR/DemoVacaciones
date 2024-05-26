from .models import Trabajadores, Vacaciones, Fechas_Importantes,Fechas_Recomendadas
from rest_framework import serializers


class TrabajadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trabajadores
        fields = ['id', 'nombre', 'apellido', 'diasVacaciones']

class TrabajadorDiasVacacionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #####
        model = Trabajadores
        fields = ['diasVacaciones']

class VacacionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacaciones
        fields = ['fechaInicio','fechaFinal','idTrabajador']

class VacacionesSerializerWXO(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacaciones
        fields = ['fechaInicio','fechaFinal','idTrabajador']

class FechasImportantesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fechas_Importantes
        fields = ['fechaInicio','fechaFinal','nombreEvento']

class FechasOpcionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fechas_Importantes
        fields = ['fechaInicio','fechaFinal']

class FechasOpcionesStringSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fechas_Recomendadas
        fields = ['fecha']