from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views

router = DefaultRouter()

# router.register(r'parentesco',views.ParentescoViewSet,basename='parentesco')
router.register(r'movilidad',views.MovilidadViewSet,basename='movilidad')
router.register(r'grado',views.GradoViewSet,basename='grado')

urlpatterns = router.urls 