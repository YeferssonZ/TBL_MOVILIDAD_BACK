from rest_framework import viewsets

from .models import *
from .serializers import *

class ParentescoViewSet(viewsets.ModelViewSet):
    queryset = TblParentesco.objects.all()
    serializer_class = ParentescoSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = TblAlumno.objects.all()
    serializer_class = AlumnoSerializer

class ColegioViewSet(viewsets.ModelViewSet):
    queryset = TblColegio.objects.all()
    serializer_class = ColegioSerializer

class ZonaViewSet(viewsets.ModelViewSet):
    queryset = TblZona.objects.all()
    serializer_class = ZonaSerializer

class ApoderadoViewSet(viewsets.ModelViewSet):
    queryset = TblApoderado.objects.all()
    serializer_class = ApoderadoSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = TblVehiculo.objects.all()
    serializer_class = VehiculoSerializer

class MovilidadViewSet(viewsets.ModelViewSet):
    queryset = TblMovilidad.objects.all()
    serializer_class = MovilidadSerializer

class GradoViewSet(viewsets.ModelViewSet):
    queryset = TblGrado.objects.all()
    serializer_class = GradoSerializer