from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'c_cliente', views.c_clienteViewSet)
router.register(r'c_rol', views.c_rolViewSet)
router.register(r'c_dispensacion', views.c_dispensacionViewSet)
router.register(r'c_receta_medica', views.c_receta_medicaViewSet)
router.register(r'c_receta_medica_detalles', views.c_receta_medica_detallesViewSet)
router.register(r'c_inventario', views.c_inventarioViewSet)


urlpatterns = [
	path('api/v1',include(router.urls))
]

