from rest_framework import serializers


from .models import *

class ParentescoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblParentesco
        fields = '__all__'

class MovilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblMovilidad
        fields = '__all__'

class GradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblGrado
        fields = '__all__'

        