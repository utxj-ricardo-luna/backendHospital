from rest_framework import viewsets
from .models import CalendarioCirugia, c_cliente,c_rol,c_inventario,c_dispensacion,c_receta_medica,c_receta_medica_detalles,ServiciosMedicos,ServiciosHospitalarios,AprobacionesServicios,BitacoraDG
from .serializer import CalendarioCirugiaSerializer, c_clienteSerializer,c_rolSerializer,c_inventarioSerializer,c_clienteSerializer,c_dispensacionSerializer,c_receta_medicaSerializer,c_receta_medica_detallesSerializer, ServiciosMedicosSerializer, ServiciosHospitalariosSerializer, AprobacionesServiciosSerializer,BitacoraDGServiciosSerializer

class c_clienteViewSet(viewsets.ModelViewSet):
	queryset = c_cliente.objects.all()
	serializer_class = c_clienteSerializer

class c_rolViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = c_rolSerializer

class CalendarioCirugiaViewSet(viewsets.ModelViewSet):
	queryset = CalendarioCirugia.objects.all()
	serializer_class = CalendarioCirugiaSerializer

class c_inventarioViewSet(viewsets.ModelViewSet):
	queryset = c_inventario.objects.all()
	serializer_class = c_inventarioSerializer

class c_dispensacionViewSet(viewsets.ModelViewSet):
	queryset = c_dispensacion.objects.all()
	serializer_class = c_dispensacionSerializer

class c_receta_medicaViewSet(viewsets.ModelViewSet):
	queryset = c_receta_medica.objects.all()
	serializer_class = c_receta_medicaSerializer

class c_receta_medica_detallesViewSet(viewsets.ModelViewSet):
	queryset = c_receta_medica_detalles.objects.all()
	serializer_class = c_receta_medica_detallesSerializer

class ServiciosMedicosViewSet(viewsets.ModelViewSet):
	queryset = ServiciosMedicos.objects.all()
	serializer_class = ServiciosMedicosSerializer

class ServiciosHospitalariosViewSet(viewsets.ModelViewSet):
	queryset = ServiciosHospitalarios.objects.all()
	serializer_class = ServiciosHospitalariosSerializer

class AprobacionesServiciosViewSet(viewsets.ModelViewSet):
	queryset = AprobacionesServicios.objects.all()
	serializer_class = AprobacionesServiciosSerializer

class BitacoraDGServiciosViewSet(viewsets.ModelViewSet):
	queryset = BitacoraDG.objects.all()
	serializer_class = BitacoraDGServiciosSerializer





