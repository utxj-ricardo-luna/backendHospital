from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'c_cliente', views.c_clienteViewSet)
router.register(r'c_rol', views.c_rolViewSet)
router.register(r'c_cirugias', views.c_rolViewSet)
router.register(r'c_Solicitud_Cirugias',views.c_rolViewSet)

urlpatterns = [
	path('api/v1',include(router.urls))
]

