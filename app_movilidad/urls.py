from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views

router = DefaultRouter()

router.register(r'parentesco',views.ParentescoViewSet,basename='parentesco')
router.register(r'alumno',views.AlumnoViewSet,basename='alumno')
router.register(r'colegio',views.ColegioViewSet,basename='colegio')
router.register(r'zona',views.ZonaViewSet,basename='zona')
router.register(r'apoderado',views.ApoderadoViewSet,basename='apoderado')
router.register(r'vehiculo',views.VehiculoViewSet,basename='vehiculo')
router.register(r'movilidad',views.MovilidadViewSet,basename='movilidad')
router.register(r'grado',views.GradoViewSet,basename='grado')

urlpatterns = router.urls 