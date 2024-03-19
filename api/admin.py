from django.contrib import admin
from .models import c_cliente,c_rol, ServiciosMedicos, ServiciosHospitalarios, AprobacionesServicios,BitacoraDG

# Register your models here.
admin.site.register(c_cliente)
admin.site.register(c_rol)
admin.site.register(ServiciosMedicos)
admin.site.register(ServiciosHospitalarios)
admin.site.register(AprobacionesServicios)
admin.site.register(BitacoraDG)