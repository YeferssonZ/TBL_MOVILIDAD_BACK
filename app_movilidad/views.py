from rest_framework import viewsets

from .models import *
from .serializers import *

class ParentescoViewSet(viewsets.ModelViewSet):
    queryset = TblParentesco.objects.all()
    serializer_class = ParentescoSerializer

class MovilidadViewSet(viewsets.ModelViewSet):
    queryset = TblMovilidad.objects.all()
    serializer_class = MovilidadSerializer

class GradoViewSet(viewsets.ModelViewSet):
    queryset = TblGrado.objects.all()
    serializer_class = GradoSerializer