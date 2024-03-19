
from rest_framework import serializers
from .models import c_cliente, c_rol, c_dispensacion, c_inventario, c_receta_medica, c_receta_medica_detalles

class c_clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = c_cliente
        fields = '__all__'
        
class c_rolSerializer(serializers.ModelSerializer):
    class Meta:
        model = c_rol
        fields = '__all__'
  
class c_dispensacionSerializer(serializers.ModelSerializer):  # Renombrado a c_dispensacionSerializer
    class Meta:
        model = c_dispensacion
        fields = '__all__'
  
class c_inventarioSerializer(serializers.ModelSerializer):  # Renombrado a c_inventarioSerializer
    class Meta:
        model = c_inventario
        fields = '__all__'
  
class c_receta_medicaSerializer(serializers.ModelSerializer):  # Renombrado a c_receta_medicaSerializer
    class Meta:
        model = c_receta_medica
        fields = '__all__'
  
class c_receta_medica_detallesSerializer(serializers.ModelSerializer):  # Renombrado a c_receta_medica_detallesSerializer
    class Meta:
        model = c_receta_medica_detalles
        fields = '__all__'



