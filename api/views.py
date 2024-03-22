from rest_framework import viewsets
from .models import c_cliente,c_rol,c_registrosM, nacimientosBebes, SeguimientoPediatrico,solicitud_organos_1, Puesto, Horario, Personal, c_cliente,c_rol,c_inventario,c_dispensacion,c_receta_medica,c_receta_medica_detalles,ServiciosMedicos,ServiciosHospitalarios,AprobacionesServicios,BitacoraDG
from .serializer import c_clienteSerializer,c_rolSerializer,c_registroSerializer,BebeSerializer, BebeCrearSerializer, SeguimientoPediatricoSerializer, SeguimientoPediatricoCrearSerializer ,solicitud_organos_1Serializer,c_inventarioSerializer,c_clienteSerializer,c_dispensacionSerializer,c_receta_medicaSerializer,c_receta_medica_detallesSerializer, ServiciosMedicosSerializer, ServiciosHospitalariosSerializer, AprobacionesServiciosSerializer,BitacoraDGServiciosSerializer, PuestoSerializer, HorarioSerializer, PersonalSerializer


# Vista para ver todos los bebés
class BebeList(generics.ListAPIView):
    queryset = nacimientosBebes.objects.all()
    serializer_class = BebeSerializer

# Vista para ver detalles de un bebé
class BebeDetail(generics.RetrieveAPIView):
    queryset = nacimientosBebes.objects.all()
    serializer_class = BebeSerializer

# Vista para crear un bebé
class BebeCrear(generics.CreateAPIView):
    serializer_class = BebeCrearSerializer

# Vista para ver todos los seguimientos pediátricos
class SeguimientoPediatricoList(generics.ListAPIView):
    queryset = SeguimientoPediatrico.objects.all()
    serializer_class = SeguimientoPediatricoSerializer

# Vista para ver detalles de un seguimiento pediátrico
class SeguimientoPediatricoDetail(generics.RetrieveAPIView):
    queryset = SeguimientoPediatrico.objects.all()
    serializer_class = SeguimientoPediatricoSerializer

# Vista para crear un seguimiento pediátrico
class SeguimientoPediatricoCrear(generics.CreateAPIView):
    serializer_class = SeguimientoPediatricoCrearSerializer
    

class c_clienteViewSet(viewsets.ModelViewSet):
	queryset = c_cliente.objects.all()
	serializer_class = c_clienteSerializer

class c_rolViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = c_rolSerializer
 
class c_registroViewSet(viewsets.ModelViewSet):
	queryset = c_registrosM.objects.all()
	serializer_class = c_registroSerializer
	
class solicitud_organos_1ViewSet(viewsets.ModelViewSet):
	queryset = solicitud_organos_1.objects.all()
	serializer_class = solicitud_organos_1Serializer

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

class PuestoViewSet(viewsets.ModelViewSet):
	queryset = Puesto.objects.all()
	serializer_class = PuestoSerializer

class HorarioViewSet(viewsets.ModelViewSet):
	queryset = Horario.objects.all()
	serializer_class = HorarioSerializer

class PersonalViewSet(viewsets.ModelViewSet):
	queryset = Personal.objects.all()
	serializer_class = PersonalSerializer





