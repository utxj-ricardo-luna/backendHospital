from rest_framework import viewsets
from .models import c_cliente,c_rol
from .serializer import c_clienteSerializer,c_rolSerializer,c_registroSerializer

class c_clienteViewSet(viewsets.ModelViewSet):
	queryset = c_cliente.objects.all()
	serializer_class = c_clienteSerializer
	
class c_rolViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = c_rolSerializer
 
class c_registroViewSet(viewsets.ModelViewSet):
	queryset = c_rol.objects.all()
	serializer_class = c_registroSerializer
