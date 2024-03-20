


from rest_framework import viewsets
from .models import c_cliente,c_rol
from .serializer import c_clienteSerializer,c_rolSerializer,c_inventario,c_cliente,c_dispensacion,c_receta_medica,c_receta_medica_detalles,c_rol
from .serializer import c_clienteSerializer,c_rolSerializer, ServiciosMedicosSerializer, ServiciosHospitalariosSerializer, AprobacionesServiciosSerializer,BitacoraDGServiciosSerializer

class c_clienteViewSet(viewsets.ModelViewSet):
	queryset = c_cliente.objects.all()
	serializer_class = c_clienteSerializer
	
class c_rolViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = c_rolSerializer

class c_inventarioViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = c_inventario
class c_dispensacionViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = c_dispensacion
class c_receta_medicaViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = c_receta_medica
class c_receta_medica_detallesViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = c_receta_medica_detalles
class ServiciosMedicosViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = ServiciosMedicosSerializer

class ServiciosHospitalariosViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = ServiciosHospitalariosSerializer

class AprobacionesServiciosViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = AprobacionesServiciosSerializer

class BitacoraDGServiciosViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = BitacoraDGServiciosSerializer





