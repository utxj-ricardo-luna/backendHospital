from rest_framework import serializers
from .models import c_cliente,c_rol, c_cirugia,c_Solicitud_Cirugias

class c_clienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = c_cliente
		fields = '__all__'
		
class c_rolSerializer(serializers.ModelSerializer):
	class Meta:
		model = c_rol
		fields = '__all__'

class c_rolSerializer(serializers.ModelSerializer):
	class Meta:
		model = c_cirugia
		fields = '__all__'

class c_Solicitud_Cirugias(serializers.ModelSerializer):
	class Meta:
		model= c_Solicitud_Cirugias
		fields= '__all__'