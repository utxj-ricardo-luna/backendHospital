from rest_framework import serializers
from .models import c_cliente,c_rol, c_registrosM

class c_clienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = c_cliente
		fields = '__all__'
		
class c_rolSerializer(serializers.ModelSerializer):
	class Meta:
		model = c_rol
		fields = '__all__'
  
class c_registroSerializer(serializers.ModelSerializer):
	class Meta:
		model = c_registrosM
		fields = '__all__'