from rest_framework import viewsets
from .models import nacimientos_bebes,seguimiento_pediatria
from .serializer import nacimientos_bebesSerializer,seguimiento_pediatriaSerializer

class nacimientos_bebesViewSet(viewsets.ModelViewSet):
	queryset = nacimientos_bebes.objects.all()
	serializer_class = nacimientos_bebesSerializer
	
class seguimiento_pediatriaViewSet(viewsets.ModelViewSet):
	queryset = seguimiento_pediatria.objects.all()
	serializer_class = seguimiento_pediatriaSerializer
