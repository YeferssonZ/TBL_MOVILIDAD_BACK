from rest_framework import serializers


from .models import *

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblAlumno
        fields = '__all__'

class ParentescoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblParentesco
        fields = '__all__'

class ColegioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblColegio
        fields = '__all__'

    def to_representation(self,instance):
        
        representation = super().to_representation(instance)
        representation['zona_nombre'] = instance.zona.zona_nombre
        return representation

class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblZona
        fields = '__all__'

class ApoderadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblApoderado
        fields = '__all__'

    def to_representation(self,instance):
        
        representation = super().to_representation(instance)
        representation['parentesco_nombre'] = instance.parentesco.parentesco_nombre
        return representation

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblVehiculo
        fields = '__all__'

class MovilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblMovilidad
        fields = '__all__'

    def to_representation(self,instance):
        
        representation = super().to_representation(instance)
        representation['colegio_nombre'] = instance.colegio.colegio_nombre
        representation['apoderado_nombre'] = instance.apoderado.apoderado_nombre
        representation['grado_nombre'] = instance.grado.grado_nombre
        representation['vehiculo_marca'] = instance.vehiculo.vehiculo_marca
        representation['alumno_nombre'] = instance.alumno.alumno_nombre
        
        return representation

class GradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblGrado
        fields = '__all__'

        