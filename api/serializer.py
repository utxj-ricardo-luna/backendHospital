from rest_framework import serializers
from .models import c_cliente,c_rol, solicitud_organos_1

class c_clienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = c_cliente
		fields = '__all__'
		
class c_rolSerializer(serializers.ModelSerializer):
	class Meta:
		model = c_rol
		fields = '__all__'
  
  
class solicitud_organos_1Serializer(serializers.ModelSerializer):
	class Meta:
		model = solicitud_organos_1
		fields = '__all__'