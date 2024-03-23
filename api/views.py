from rest_framework import viewsets
from .models import c_cliente,c_rol,c_registrosM, nacimientos_bebes,seguimiento_pediatria,solicitud_organos_1, Puesto, Horario, Personal, c_cliente,c_rol, c_dispensacion_medicamentos,c_detalle_dispensacion,c_detalle_dispensacion_relacion, c_lotes_medicamentos,c_detalle_lotes,ServiciosMedicos,ServiciosHospitalarios,AprobacionesServicios,BitacoraDG
from .serializer import c_clienteSerializer,c_rolSerializer,c_registroSerializer, nacimientos_bebesSerializer,seguimiento_pediatriaSerializer,solicitud_organos_1Serializer,c_clienteSerializer,c_dispensacionSerializer,c_detalle_dispensacionSerializer,c_lotesSerializer,c_detalle_lotesSerializer,c_detalle_dispensacion_relacionSerializer, ServiciosMedicosSerializer, ServiciosHospitalariosSerializer, AprobacionesServiciosSerializer,BitacoraDGServiciosSerializer, PuestoSerializer, HorarioSerializer, PersonalSerializer

class nacimientos_bebesViewSet(viewsets.ModelViewSet):
	queryset = nacimientos_bebes.objects.all()
	serializer_class = nacimientos_bebesSerializer
	
class seguimiento_pediatriaViewSet(viewsets.ModelViewSet):
	queryset = seguimiento_pediatria.objects.all()
	serializer_class = seguimiento_pediatriaSerializer

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

#FARMACIA
class c_dispensacionViewSet(viewsets.ModelViewSet):
	queryset = c_dispensacion_medicamentos.objects.all()
	serializer_class = c_dispensacionSerializer

class c_detalle_dispensacionViewSet(viewsets.ModelViewSet):
	queryset = c_detalle_dispensacion.objects.all()
	serializer_class = c_detalle_dispensacionSerializer

class c_detalle_dispensacion_relacionViewSet(viewsets.ModelViewSet):
	queryset = c_detalle_dispensacion_relacion.objects.all()
	serializer_class = c_detalle_dispensacion_relacionSerializer


class c_lotes_medicamentoViewSet(viewsets.ModelViewSet):
	queryset = c_lotes_medicamentos.objects.all()
	serializer_class = c_lotesSerializer

class c_detalle_lotes_medicamentoViewSet(viewsets.ModelViewSet):
	queryset = c_detalle_lotes.objects.all()
	serializer_class = c_detalle_lotesSerializer



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





