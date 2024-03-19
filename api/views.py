from rest_framework import viewsets
from .models import c_cliente,c_rol, solicitud_organos_1
from .serializer import c_clienteSerializer,c_rolSerializer, solicitud_organos_1Serializer

class c_clienteViewSet(viewsets.ModelViewSet):
	queryset = c_cliente.objects.all()
	serializer_class = c_clienteSerializer
	
class c_rolViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = c_rolSerializer
	
class solicitud_organos_1ViewSet(viewsets.ModelViewSet):
	queryset = solicitud_organos_1.objects.all()
	serializer_class = solicitud_organos_1Serializer
