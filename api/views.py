from rest_framework import viewsets
from .models import CalendarioCirugia, c_cliente,c_rol
from .serializer import CalendarioCirugiaSerializer, c_clienteSerializer,c_rolSerializer

class c_clienteViewSet(viewsets.ModelViewSet):
	queryset = c_cliente.objects.all()
	serializer_class = c_clienteSerializer
	
class c_rolViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = c_rolSerializer


class CalendarioCirugiaViewSet(viewsets.ModelViewSet):
	queryset = CalendarioCirugia.objects.all()
	serializer_class = CalendarioCirugiaSerializer