from rest_framework import serializers
from .models import CalendarioCirugia, c_cliente,c_rol

class c_clienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = c_cliente
		fields = '__all__'
		
class c_rolSerializer(serializers.ModelSerializer):
	class Meta:
		model = c_rol
		fields = '__all__'

class CalendarioCirugiaSerializer(serializers.ModelSerializer):
	class Meta:
		model = CalendarioCirugia
		fields = '__all__'
